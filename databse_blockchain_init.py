import sqlite3
import os

# Caminho para a criação do banco de dados
db_dir = "app/db"
os.makedirs(db_dir, exist_ok=True)
db_path = os.path.join(db_dir, "consensus_network.db")

# Conexão com o banco de dados SQLite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Função para criar as tabelas do banco de dados
def create_consensus_tables():
    # Grupo 1: Mineração
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS mining_nodes (
        id INTEGER PRIMARY KEY,
        node_name TEXT NOT NULL,
        hash_rate REAL NOT NULL,
        power_consumption REAL,
        mining_algorithm TEXT CHECK(mining_algorithm IN ('PoW', 'PoS', 'PoH')) NOT NULL,
        status TEXT CHECK(status IN ('active', 'inactive')) NOT NULL
    )
    ''')

    # Grupo 2: Staking
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS staking_pools (
        id INTEGER PRIMARY KEY,
        pool_name TEXT NOT NULL,
        total_staked REAL NOT NULL,
        reward_rate REAL NOT NULL,
        validator_count INTEGER,
        pool_status TEXT CHECK(pool_status IN ('open', 'closed')) NOT NULL
    )
    ''')

    # Grupo 3: Algoritmos de Consenso
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS consensus_algorithms (
        id INTEGER PRIMARY KEY,
        algorithm_name TEXT NOT NULL,
        type TEXT CHECK(type IN ('PoW', 'PoS', 'DPoS', 'PBFT', 'Raft')) NOT NULL,
        block_time REAL NOT NULL,
        finality_time REAL NOT NULL,
        fault_tolerance REAL CHECK(fault_tolerance <= 1.0) NOT NULL,
        description TEXT
    )
    ''')

    # Grupo 4: Transações
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        sender_node_id INTEGER,
        receiver_node_id INTEGER,
        transaction_amount REAL NOT NULL,
        consensus_algorithm_id INTEGER,
        timestamp TEXT NOT NULL,
        tx_hash TEXT UNIQUE NOT NULL,
        status TEXT CHECK(status IN ('pending', 'completed', 'failed')) NOT NULL,
        FOREIGN KEY(consensus_algorithm_id) REFERENCES consensus_algorithms(id),
        FOREIGN KEY(sender_node_id) REFERENCES mining_nodes(id),
        FOREIGN KEY(receiver_node_id) REFERENCES mining_nodes(id)
    )
    ''')

    # Grupo 5: Tolerância a Falhas (Fault Tolerance)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS fault_tolerance_metrics (
        id INTEGER PRIMARY KEY,
        node_id INTEGER,
        fault_tolerance_score REAL CHECK(fault_tolerance_score <= 1.0) NOT NULL,
        downtime_percentage REAL NOT NULL,
        recovery_time REAL,
        FOREIGN KEY(node_id) REFERENCES mining_nodes(id)
    )
    ''')

    # Grupo 6: Requisições e Respostas (Replying)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS node_responses (
        id INTEGER PRIMARY KEY,
        request_id INTEGER,
        node_id INTEGER,
        response_time REAL NOT NULL,
        status TEXT CHECK(status IN ('success', 'failure', 'timeout')) NOT NULL,
        FOREIGN KEY(node_id) REFERENCES mining_nodes(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS network_requests (
        id INTEGER PRIMARY KEY,
        sender_node_id INTEGER,
        request_type TEXT CHECK(request_type IN ('transaction', 'data', 'state')) NOT NULL,
        request_time REAL NOT NULL,
        FOREIGN KEY(sender_node_id) REFERENCES mining_nodes(id)
    )
    ''')

    # Grupo 7: Tolerância a Falhas em Sistemas de Dados (No-Failure)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS data_no_failure_scenarios (
        id INTEGER PRIMARY KEY,
        node_id INTEGER,
        scenario_description TEXT NOT NULL,
        fault_tolerance_algorithm_id INTEGER,
        FOREIGN KEY(node_id) REFERENCES mining_nodes(id),
        FOREIGN KEY(fault_tolerance_algorithm_id) REFERENCES consensus_algorithms(id)
    )
    ''')

    # Grupo 8: Envio e Troca de Dados (Data Sender and Exchange)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS data_exchange_logs (
        id INTEGER PRIMARY KEY,
        sender_node_id INTEGER,
        receiver_node_id INTEGER,
        data_size REAL NOT NULL,
        timestamp TEXT NOT NULL,
        status TEXT CHECK(status IN ('sent', 'received', 'failed')) NOT NULL,
        FOREIGN KEY(sender_node_id) REFERENCES mining_nodes(id),
        FOREIGN KEY(receiver_node_id) REFERENCES mining_nodes(id)
    )
    ''')

    # Grupo 9: Nós de Rede Blockchain (Network Nodes)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS blockchain_network_nodes (
        id INTEGER PRIMARY KEY,
        node_name TEXT NOT NULL,
        node_type TEXT CHECK(node_type IN ('full', 'light', 'archive')) NOT NULL,
        consensus_algorithm_id INTEGER,
        stake REAL,
        node_status TEXT CHECK(node_status IN ('active', 'inactive')) NOT NULL,
        FOREIGN KEY(consensus_algorithm_id) REFERENCES consensus_algorithms(id)
    )
    ''')

    # Grupo 10: Contratos Inteligentes (Smart Contracts)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS smart_contracts (
        id INTEGER PRIMARY KEY,
        contract_name TEXT NOT NULL,
        bytecode TEXT NOT NULL,
        creator_node_id INTEGER,
        status TEXT CHECK(status IN ('active', 'inactive')) NOT NULL,
        creation_date TEXT NOT NULL,
        FOREIGN KEY(creator_node_id) REFERENCES blockchain_network_nodes(id)
    )
    ''')

    # Grupo 11: Estado da Rede
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS network_state_snapshots (
        id INTEGER PRIMARY KEY,
        node_id INTEGER,
        block_height INTEGER NOT NULL,
        state_hash TEXT NOT NULL,
        timestamp TEXT NOT NULL,
        FOREIGN KEY(node_id) REFERENCES blockchain_network_nodes(id)
    )
    ''')

    # Grupo 12: Relatórios de Consenso
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS consensus_reports (
        id INTEGER PRIMARY KEY,
        algorithm_id INTEGER,
        total_nodes INTEGER,
        avg_block_time REAL,
        avg_finality_time REAL,
        FOREIGN KEY(algorithm_id) REFERENCES consensus_algorithms(id)
    )
    ''')

# Executa a criação das tabelas
create_consensus_tables()

# Confirma e fecha a conexão
conn.commit()
conn.close()

print(f"Banco de dados 'consensus_network.db' criado com sucesso em {db_path}")
