import os

# Define o caminho do projeto
project_path = r"C:\caminho\para\tokenomics_backend\app"

# Cria as pastas principais
folders = [
    "application",
    "background_tasks",
    "ci_cd",
    "config",
    "controllers",
    "database",
    "domain",
    "events",
    "infra/ansible",
    "infra/docker",
    "infra/gitops",
    "infra/kubernetes",
    "infra/terraform",
    "infrastructure",
    "middlewares",
    "models",
    "presentation",
    "routes",
    "schemas",
    "scripts",
    "services",
    "tests",
    "utils"
]

# Cria as pastas
for folder in folders:
    os.makedirs(os.path.join(project_path, folder), exist_ok=True)

# Cria arquivos .py vazios nas pastas apropriadas
files = [
    "application/__init__.py",
    "background_tasks/__init__.py",
    "ci_cd/pipeline.yaml",
    "config/app.py",
    "config/config.py",
    "config/logging.yaml",
    "config/settings.yaml",
    "config/__init__.py",
    "controllers/app.py",
    "controllers/config.py",
    "controllers/__init__.py",
    "database/app.py",
    "database/config.py",
    "database/__init__.py",
    "infra/ansible/playbook.yaml",
    "infra/docker/Dockerfile",
    "infra/gitops/config.yaml",
    "infra/kubernetes/deployment.yaml",
    "infra/terraform/main.tf",
    "infrastructure/__init__.py",
    "middlewares/app.py",
    "middlewares/config.py",
    "middlewares/__init__.py",
    "models/app.py",
    "models/config.py",
    "models/__init__.py",
    "presentation/__init__.py",
    "routes/app.py",
    "routes/config.py",
    "routes/__init__.py",
    "schemas/app.py",
    "schemas/config.py",
    "schemas/__init__.py",
    "scripts/setup.sh",
    "scripts/start.sh",
    "services/app.py",
    "services/config.py",
    "services/__init__.py",
    "tests/app.py",
    "tests/config.py",
    "tests/__init__.py",
    "utils/app.py",
    "utils/config.py",
    "utils/__init__.py"
]

# Cria arquivos vazios
for file in files:
    open(os.path.join(project_path, file), 'a').close()

print(f"Estrutura de pastas e arquivos criada com sucesso em {project_path}")
