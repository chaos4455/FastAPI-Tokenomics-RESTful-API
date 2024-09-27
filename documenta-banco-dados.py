import os
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
                db_files.append({
                    "name": file,
                    "location": db_path,
                    "size_bytes": os.path.getsize(db_path),
                    "created": datetime.fromtimestamp(os.path.getctime(db_path)).isoformat(),
                    "modified": datetime.fromtimestamp(os.path.getmtime(db_path)).isoformat()
                })
    return db_files

# Encontrar todos os arquivos .db
database_files = find_databases(project_root)

# Preparar para exportar para YAML
yaml_output = {
    "project": {
        "name": "Tokenomics Backend Project",
        "description": "Documentação dos bancos de dados encontrados na estrutura do projeto.",
        "version": "1.0",
        "databases": database_files
    }
}

# Estilização dos ícones e emojis
yaml_styled_output = yaml.dump(yaml_output, allow_unicode=True, sort_keys=False)

# Caminho para o arquivo YAML
yaml_file_path = os.path.join(project_root, "databases_structure.yaml")

# Exportar para YAML
with open(yaml_file_path, "w", encoding='utf-8') as yaml_file:
    yaml_file.write("# 🗄️ Estrutura dos Bancos de Dados\n")
    yaml_file.write("# 📄 Detalhes dos arquivos .db encontrados na estrutura do projeto.\n")
    yaml_file.write("# 📅 Versão: 1.0\n\n")
    yaml_file.write(yaml_styled_output)

print(f"Documentação dos bancos de dados exportada para: {yaml_file_path}")
