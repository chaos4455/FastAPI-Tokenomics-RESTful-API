import os
import yaml

# Caminho para a pasta do projeto
project_root = "tokenomics_backend"

def generate_structure(path):
    structure = {}
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):  # Se for um diretório
            structure[item] = generate_structure(item_path)  # Recursão
        else:  # Se for um arquivo
            structure[item] = None  # Apenas registramos o nome do arquivo
    return structure

# Gerar a estrutura
project_structure = generate_structure(project_root)

# Preparar para exportar para YAML
yaml_output = {
    "project": {
        "name": "Tokenomics Backend Project",
        "description": "Estrutura do projeto API FastAPI com foco em Tokenomics.",
        "version": "1.0",
        "structure": project_structure
    }
}

# Estilização dos ícones e emojis
yaml_styled_output = yaml.dump(yaml_output, allow_unicode=True, sort_keys=False)

# Caminho para o arquivo YAML
yaml_file_path = os.path.join(project_root, "directory_structure.yaml")

# Exportar para YAML
with open(yaml_file_path, "w", encoding='utf-8') as yaml_file:
    yaml_file.write("# 🚀 Estrutura do Projeto: Tokenomics Backend\n")
    yaml_file.write("# 📝 Descrição: Documentação da estrutura de pastas e arquivos.\n")
    yaml_file.write("# 📅 Versão: 1.0\n\n")
    yaml_file.write(yaml_styled_output)

print(f"Documentação da estrutura do projeto exportada para: {yaml_file_path}")
