# app/main.py

from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
import os
import logging
import logging.config
import yaml
import asyncio
import aiosqlite
from typing import Dict, Any

# Importar a função de configuração de logging
from app.utils.logging_config import load_logging_config

# Configurar logging
try:
    load_logging_config()
except Exception as e:
    print(f"Erro ao carregar configurações de logging: {e}")

# Criar a aplicação FastAPI
app = FastAPI()

# Definição do router
router = APIRouter()

# Caminho do banco de dados
DB_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db'))
DB_PATH = os.path.join(DB_DIR, "network_database.db")

# Fila de operações
db_queue = asyncio.Queue()

async def db_worker():
    """Processar operações na fila do banco de dados."""
    while True:
        conn, query, params, future = await db_queue.get()
        try:
            cursor = await conn.execute(query, params)
            await conn.commit()
            future.set_result(cursor)
        except Exception as e:
            future.set_exception(e)
        finally:
            db_queue.task_done()
            await conn.close()

async def start_db_worker():
    """Iniciar o worker do banco de dados em segundo plano."""
    asyncio.create_task(db_worker())

@app.on_event("startup")
async def startup_event():
    """Evento de inicialização da aplicação."""
    await start_db_worker()

async def get_db_connection():
    """Obter uma conexão com o banco de dados."""
    conn = await aiosqlite.connect(DB_PATH)
    return conn

# Modelos para Wallet
class WalletCreate(BaseModel):
    user_id: int
    public_key: str
    private_key_hash: str
    currency: str
    token_type: str

class WalletUpdate(BaseModel):
    public_key: str
    private_key_hash: str
    currency: str
    token_type: str

# Rotas para Wallets
@router.post("/wallets/", response_model=Dict[str, str])
async def create_wallet(wallet: WalletCreate):
    conn = await get_db_connection()
    future = asyncio.Future()
    await db_queue.put((
        conn,
        '''INSERT INTO wallets (user_id, public_key, private_key_hash, currency, token_type)
           VALUES (?, ?, ?, ?, ?)''',
        (wallet.user_id, wallet.public_key, wallet.private_key_hash, wallet.currency, wallet.token_type),
        future
    ))
    await future
    return {"message": "Carteira criada com sucesso."}

@router.get("/wallets/{wallet_id}", response_model=Dict[str, Any])
async def get_wallet(wallet_id: int):
    conn = await get_db_connection()
    future = asyncio.Future()
    await db_queue.put((
        conn,
        'SELECT * FROM wallets WHERE id = ?',
        (wallet_id,),
        future
    ))
    cursor = await future
    
    wallet = await cursor.fetchone()
    if wallet:
        return {key: wallet[key] for key in wallet.keys()}
    raise HTTPException(status_code=404, detail="Carteira não encontrada.")

@router.put("/wallets/{wallet_id}", response_model=Dict[str, str])
async def update_wallet(wallet_id: int, wallet: WalletUpdate):
    conn = await get_db_connection()
    future = asyncio.Future()
    await db_queue.put((
        conn,
        '''UPDATE wallets SET public_key = ?, private_key_hash = ?, currency = ?, token_type = ?
           WHERE id = ?''',
        (wallet.public_key, wallet.private_key_hash, wallet.currency, wallet.token_type, wallet_id),
        future
    ))
    await future
    return {"message": "Carteira atualizada com sucesso."}

@router.delete("/wallets/{wallet_id}", response_model=Dict[str, str])
async def delete_wallet(wallet_id: int):
    conn = await get_db_connection()
    future = asyncio.Future()
    await db_queue.put((
        conn,
        'DELETE FROM wallets WHERE id = ?',
        (wallet_id,),
        future
    ))
    await future
    return {"message": "Carteira deletada com sucesso."}

# [Repita o mesmo padrão para as outras entidades (Users, Tokens, Transactions, SmartContracts, Products, Clients)]
# Exemplos:
# Users, Tokens, Transactions, SmartContracts, Products e Clients serão implementados de forma semelhante,
# seguindo a mesma estrutura para garantir consistência.

# Incluir o router na aplicação
app.include_router(router)

# Definir o ponto de entrada
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
