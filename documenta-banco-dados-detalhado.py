import os
import sqlite3
import yaml
from datetime import datetime

# Caminho para a pasta do projeto
project_root = "tokenomics_backend"

def find_databases(path):
    db_files = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith('.db'):
                db_path = os.path.join(root, file)
                db_files.append(db_path)
    return db_files

def analyze_database(db_path):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Coletar informações sobre as tabelas
    tables_info = []
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for (table_name,) in tables:
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        
        table_details = {
            "table_name": table_name,
            "columns": []
        }

        for column in columns:
            col_details = {
                "column_name": column[1],
                "data_type": column[2],
                "not_null": bool(column[3]),
                "default_value": column[4],
                "primary_key": bool(column[5]),
            }
            table_details["columns"].append(col_details)
        
        tables_info.append(table_details)

    connection.close()
    
    return {
        "name": os.path.basename(db_path),
        "location": db_path,
        "tables": tables_info,
        "size_bytes": os.path.getsize(db_path),
        "created": datetime.fromtimestamp(os.path.getctime(db_path)).isoformat(),
        "modified": datetime.fromtimestamp(os.path.getmtime(db_path)).isoformat()
    }

# Encontrar todos os arquivos .db
database_files = find_databases(project_root)

# Analisar cada banco de dados encontrado
detailed_databases_info = []
for db in database_files:
    detailed_info = analyze_database(db)
    detailed_databases_info.append(detailed_info)

# Preparar para exportar para YAML
yaml_output = {
    "project": {
        "name": "Tokenomics Backend Project",
        "description": "Documentação detalhada dos bancos de dados encontrados na estrutura do projeto.",
        "version": "1.0",
        "databases": detailed_databases_info
    }
}

# Estilização dos ícones e emojis
yaml_styled_output = yaml.dump(yaml_output, allow_unicode=True, sort_keys=False)

# Caminho para o arquivo YAML
yaml_file_path = os.path.join(project_root, "databases_structure_detailed.yaml")

# Exportar para YAML
with open(yaml_file_path, "w", encoding='utf-8') as yaml_file:
    yaml_file.write("# 🗄️ Estrutura Detalhada dos Bancos de Dados\n")
    yaml_file.write("# 📄 Detalhes dos arquivos .db encontrados na estrutura do projeto.\n")
    yaml_file.write("# 📅 Versão: 1.0\n\n")
    yaml_file.write(yaml_styled_output)

print(f"Documentação detalhada dos bancos de dados exportada para: {yaml_file_path}")
