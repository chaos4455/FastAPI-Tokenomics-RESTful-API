from pydantic import BaseModel

class Wallet(BaseModel):
    id: int
    name: str
    balance: float
