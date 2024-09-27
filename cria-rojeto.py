import os

def create_project_structure(project_name):
    # Pastas principais
    folders = [
        f"{project_name}/app/domain",   # DDD - Domínio da aplicação
        f"{project_name}/app/application",  # Lógica de aplicação
        f"{project_name}/app/infrastructure",  # Camada de infraestrutura
        f"{project_name}/app/presentation",  # Camada de apresentação (FastAPI endpoints)
        f"{project_name}/app/config",  # Configurações YAML
        f"{project_name}/app/tests",  # Testes unitários e de integração
        
        # Event-Driven Design e serviços de background
        f"{project_name}/app/events",
        f"{project_name}/app/background_tasks",
        
        # Infraestrutura, DevOps e GitOps
        f"{project_name}/infra/docker",
        f"{project_name}/infra/kubernetes",
        f"{project_name}/infra/terraform",
        f"{project_name}/infra/ansible",
        f"{project_name}/infra/gitops",
        
        # Arquivos de CI/CD e scripts
        f"{project_name}/ci_cd",
        f"{project_name}/scripts",
        
        # Documentação
        f"{project_name}/docs"
    ]

    # Arquivos principais
    files = {
        f"{project_name}/app/main.py": "",  # Arquivo principal da API
        f"{project_name}/app/config/settings.yaml": "# Configurações do projeto em YAML\n",
        f"{project_name}/app/config/logging.yaml": "# Configurações de logging\n",
        f"{project_name}/app/domain/__init__.py": "",
        f"{project_name}/app/application/__init__.py": "",
        f"{project_name}/app/infrastructure/__init__.py": "",
        f"{project_name}/app/presentation/__init__.py": "",
        f"{project_name}/app/tests/__init__.py": "",
        f"{project_name}/app/events/__init__.py": "",
        f"{project_name}/app/background_tasks/__init__.py": "",
        f"{project_name}/infra/docker/Dockerfile": "# Dockerfile base\n",
        f"{project_name}/infra/kubernetes/deployment.yaml": "# Kubernetes deployment config\n",
        f"{project_name}/infra/terraform/main.tf": "# Terraform config\n",
        f"{project_name}/infra/ansible/playbook.yaml": "# Ansible playbook\n",
        f"{project_name}/infra/gitops/config.yaml": "# GitOps configuration\n",
        f"{project_name}/ci_cd/pipeline.yaml": "# Pipeline de CI/CD\n",
        f"{project_name}/docs/README.md": "# Documentação do projeto\n",
        f"{project_name}/scripts/setup.sh": "# Script de setup\n",
        f"{project_name}/scripts/start.sh": "# Script para iniciar o projeto\n",
        f"{project_name}/.gitignore": "# Arquivos a serem ignorados pelo git\n__pycache__/\n.env\n"
    }

    # Criar as pastas
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    # Criar os arquivos
    for file_path, content in files.items():
        with open(file_path, 'w') as f:
            f.write(content)

    print(f"Estrutura do projeto '{project_name}' criada com sucesso!")

# Executa a função para criar o projeto
create_project_structure("tokenomics_backend")
