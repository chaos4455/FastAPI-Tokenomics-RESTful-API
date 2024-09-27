import sqlite3
import os

# Caminho do banco de dados na pasta "db" dentro de "app"
db_dir = "app/db"
os.makedirs(db_dir, exist_ok=True)
db_path = os.path.join(db_dir, "network_database.db")

# Conexão com o banco de dados SQLite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Função para criar as tabelas e colunas do banco de dados
def create_tables():
    # Grupo 1: Informações de Usuários
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        password_hash TEXT NOT NULL,
        user_type TEXT CHECK(user_type IN ('B2B', 'B2C')) NOT NULL,
        creation_date TEXT,
        country TEXT,
        status TEXT CHECK(status IN ('active', 'inactive'))
    )
    ''')
    
    # Grupo 2: Carteiras e Tokens
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS wallets (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        public_key TEXT UNIQUE NOT NULL,
        private_key_hash TEXT NOT NULL,
        token_balance REAL DEFAULT 0,
        currency TEXT NOT NULL,
        token_type TEXT CHECK(token_type IN ('HTS', 'Hbar')) NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    ''')
    
    # Grupo 3: Tokens
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tokens (
        id INTEGER PRIMARY KEY,
        token_name TEXT NOT NULL,
        token_symbol TEXT NOT NULL,
        total_supply REAL NOT NULL,
        decimal_places INTEGER DEFAULT 18,
        token_type TEXT CHECK(token_type IN ('fungible', 'non-fungible')) NOT NULL,
        creation_date TEXT
    )
    ''')
    
    # Grupo 4: Transações
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        sender_wallet_id INTEGER,
        receiver_wallet_id INTEGER,
        amount REAL NOT NULL,
        token_id INTEGER NOT NULL,
        timestamp TEXT NOT NULL,
        tx_hash TEXT UNIQUE NOT NULL,
        status TEXT CHECK(status IN ('pending', 'completed', 'failed')) NOT NULL,
        FOREIGN KEY(sender_wallet_id) REFERENCES wallets(id),
        FOREIGN KEY(receiver_wallet_id) REFERENCES wallets(id),
        FOREIGN KEY(token_id) REFERENCES tokens(id)
    )
    ''')
    
    # Grupo 5: Contratos Inteligentes (Smart Contracts)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS smart_contracts (
        id INTEGER PRIMARY KEY,
        contract_name TEXT NOT NULL,
        bytecode TEXT NOT NULL,
        creator_wallet_id INTEGER,
        creation_date TEXT,
        status TEXT CHECK(status IN ('active', 'inactive')) NOT NULL,
        FOREIGN KEY(creator_wallet_id) REFERENCES wallets(id)
    )
    ''')
    
    # Grupo 6: Produtos e Serviços
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL,
        token_id INTEGER NOT NULL,
        available_quantity INTEGER NOT NULL,
        FOREIGN KEY(token_id) REFERENCES tokens(id)
    )
    ''')
    
    # Grupo 7: Clientes e Fornecedores
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        contact_number TEXT,
        company_name TEXT,
        client_type TEXT CHECK(client_type IN ('B2B', 'B2C')) NOT NULL,
        creation_date TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS suppliers (
        id INTEGER PRIMARY KEY,
        supplier_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        contact_number TEXT,
        product_id INTEGER,
        service_id INTEGER,
        company_name TEXT,
        FOREIGN KEY(product_id) REFERENCES products(id),
        FOREIGN KEY(service_id) REFERENCES services(id)
    )
    ''')
    
    # Grupo 8: Pedidos e Pagamentos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        client_id INTEGER,
        product_id INTEGER,
        service_id INTEGER,
        quantity INTEGER,
        total_price REAL,
        order_status TEXT CHECK(order_status IN ('pending', 'completed', 'cancelled')) NOT NULL,
        order_date TEXT NOT NULL,
        FOREIGN KEY(client_id) REFERENCES clients(id),
        FOREIGN KEY(product_id) REFERENCES products(id),
        FOREIGN KEY(service_id) REFERENCES services(id)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS payments (
        id INTEGER PRIMARY KEY,
        order_id INTEGER,
        wallet_id INTEGER,
        payment_amount REAL NOT NULL,
        payment_status TEXT CHECK(payment_status IN ('pending', 'completed', 'failed')) NOT NULL,
        payment_date TEXT NOT NULL,
        FOREIGN KEY(order_id) REFERENCES orders(id),
        FOREIGN KEY(wallet_id) REFERENCES wallets(id)
    )
    ''')
    
    # Grupo 9: Análises e Relatórios
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS analytics (
        id INTEGER PRIMARY KEY,
        token_id INTEGER,
        daily_volume REAL,
        total_transactions INTEGER,
        average_transaction_value REAL,
        report_date TEXT NOT NULL,
        FOREIGN KEY(token_id) REFERENCES tokens(id)
    )
    ''')
    
    # Grupo 10: Infraestrutura de Rede (Blockchain Nodes)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS network_nodes (
        id INTEGER PRIMARY KEY,
        node_name TEXT NOT NULL,
        ip_address TEXT UNIQUE NOT NULL,
        public_key TEXT NOT NULL,
        stake REAL DEFAULT 0,
        node_status TEXT CHECK(node_status IN ('active', 'inactive')) NOT NULL
    )
    ''')
    
    # Grupo 11: Governança de Rede
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS governance (
        id INTEGER PRIMARY KEY,
        proposal TEXT NOT NULL,
        proposal_description TEXT,
        creation_date TEXT,
        voting_deadline TEXT,
        status TEXT CHECK(status IN ('open', 'closed')) NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS votes (
        id INTEGER PRIMARY KEY,
        proposal_id INTEGER,
        voter_wallet_id INTEGER,
        vote_value TEXT CHECK(vote_value IN ('yes', 'no')) NOT NULL,
        vote_date TEXT NOT NULL,
        FOREIGN KEY(proposal_id) REFERENCES governance(id),
        FOREIGN KEY(voter_wallet_id) REFERENCES wallets(id)
    )
    ''')
    
    # Grupo 12: Suporte e Atendimento
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS support_tickets (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        issue_description TEXT,
        issue_status TEXT CHECK(issue_status IN ('open', 'closed', 'pending')) NOT NULL,
        submission_date TEXT,
        resolution_date TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    ''')
    
    # Grupo 13: Auditoria e Logs
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS audit_logs (
        id INTEGER PRIMARY KEY,
        action TEXT NOT NULL,
        user_id INTEGER,
        timestamp TEXT NOT NULL,
        description TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    ''')

# Executa a criação das tabelas
create_tables()

# Confirma e fecha a conexão
conn.commit()
conn.close()

print(f"Banco de dados 'network_database.db' criado com sucesso em {db_path}")
