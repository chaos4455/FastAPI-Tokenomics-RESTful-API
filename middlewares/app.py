from fastapi import Request, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Callable
import logging

# Configurações de autenticação
SECRET_KEY = "123456"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("my_logger")

# Função para criar tokens
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Middleware para validar o token
async def validate_token(request: Request):
    token = request.headers.get("Authorization")
    if token is None:
        logger.warning("Tentativa de acesso não autorizado.")
        raise HTTPException(status_code=401, detail="Não autorizado")

    try:
        # Remove o prefixo 'Bearer' do token
        token = token.split(" ")[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        logger.info(f"Token válido para o usuário: {payload['sub']}")
        return payload
    except (JWTError, IndexError):
        logger.error("Token inválido ou expirado.")
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")

# Dependência para garantir que o usuário esteja autenticado
async def get_current_user(token: str = Depends(oauth2_scheme)):
    return await validate_token(token)

# Middleware de logging de requisições
async def log_requests(request: Request, call_next: Callable):
    logger.info(f"Recebendo requisição: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Resposta: {response.status_code}")
    return response
