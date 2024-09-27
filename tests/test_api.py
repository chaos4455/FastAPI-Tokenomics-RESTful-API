import httpx

# Configuração da URL base da API
BASE_URL = "http://localhost:8000"  # ajuste se necessário

# Teste para criar uma wallet
def test_create_wallet():
    response = httpx.post(f"{BASE_URL}/wallets/", json={
        "user_id": 1,
        "public_key": "sample_public_key",
        "private_key_hash": "sample_hash",
        "currency": "USD",
        "token_type": "ERC20"
    })
    print("Create Wallet Response:", response.json())

# Teste para obter uma wallet
def test_get_wallet(wallet_id):
    response = httpx.get(f"{BASE_URL}/wallets/{wallet_id}")
    print("Get Wallet Response:", response.json())

# Teste para atualizar uma wallet
def test_update_wallet(wallet_id):
    response = httpx.put(f"{BASE_URL}/wallets/{wallet_id}", json={
        "public_key": "updated_public_key",
        "private_key_hash": "updated_hash",
        "currency": "EUR",
        "token_type": "ERC20"
    })
    print("Update Wallet Response:", response.json())

# Teste para deletar uma wallet
def test_delete_wallet(wallet_id):
    response = httpx.delete(f"{BASE_URL}/wallets/{wallet_id}")
    print("Delete Wallet Response:", response.json())

# Teste para criar um usuário
def test_create_user():
    response = httpx.post(f"{BASE_URL}/users/", json={
        "name": "John Doe",
        "email": "john@example.com",
        "password_hash": "hashed_password",
        "user_type": "admin",
        "creation_date": "2024-09-27",
        "country": "USA",
        "status": "active"
    })
    print("Create User Response:", response.json())

# Teste para obter um usuário
def test_get_user(user_id):
    response = httpx.get(f"{BASE_URL}/users/{user_id}")
    print("Get User Response:", response.json())

# Teste para atualizar um usuário
def test_update_user(user_id):
    response = httpx.put(f"{BASE_URL}/users/{user_id}", json={
        "name": "John Smith",
        "email": "johnsmith@example.com",
        "user_type": "user",
        "country": "USA",
        "status": "active"
    })
    print("Update User Response:", response.json())

# Teste para deletar um usuário
def test_delete_user(user_id):
    response = httpx.delete(f"{BASE_URL}/users/{user_id}")
    print("Delete User Response:", response.json())

# Você pode fazer o mesmo para os tokens, transactions, smart_contracts, products, clients e suppliers.

# Exemplo de chamada dos testes
if __name__ == "__main__":
    # Para fins de teste, crie uma wallet e um usuário e faça as operações
    test_create_wallet()
    test_create_user()
    # Coloque aqui o ID da wallet ou do usuário que você deseja testar
    wallet_id = 1  # Substitua pelo ID correto
    user_id = 1    # Substitua pelo ID correto
    test_get_wallet(wallet_id)
    test_update_wallet(wallet_id)
    test_delete_wallet(wallet_id)
    test_get_user(user_id)
    test_update_user(user_id)
    test_delete_user(user_id)
