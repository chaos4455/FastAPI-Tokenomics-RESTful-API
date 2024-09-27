from fastapi import FastAPI
from .routes.app import router as wallet_router
from .middlewares.app import log_requests
import logging
import logging.config
import yaml
import os

# Função para carregar configurações de logging
def load_logging_config():
    config_path = "app/config/logging.yaml"
    
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"O arquivo de configuração de logging não foi encontrado: {config_path}")
    
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
        
        if config is None:
            raise ValueError("A configuração de logging não pode ser None.")
        
        logging.config.dictConfig(config)

# Criar a aplicação FastAPI
app = FastAPI()

# Configurar logging
try:
    load_logging_config()
except Exception as e:
    print(f"Erro ao carregar configurações de logging: {e}")

# Adicionar middleware de logging de requisições
app.middleware("http")(log_requests)

# Incluir o router de wallets e outras rotas
app.include_router(wallet_router, prefix="/api")

# Rota de exemplo
@app.get("/")
async def read_root():
    return {"message": "API de gerenciamento de carteiras está funcionando!"}

# Executar a aplicação
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7777)
