# 🚀 FastAPI-Tokenomics-RESTful-API

## 📝 **Descrição do Projeto**

Este projeto foi criado para consolidar meus conhecimentos em **Python** e **FastAPI**, onde venho de um background de **Flask** desde 2018 e agora estou ampliando minha stack para incluir **FastAPI**. Escolhi FastAPI devido à sua performance superior, tipagem moderna com Pydantic, e compatibilidade com sistemas assíncronos, tornando-a ideal para **microserviços** de alta escala.

A API foi construída seguindo os princípios de **DDD (Domain-Driven Design)** e **SOLID**, com um foco forte em **DRY** (Don't Repeat Yourself) para garantir um código modular e sustentável.

### ⚡ Por que **FastAPI**?

- **Performance**: FastAPI é extremamente rápida, comparável a Node.js e Go.
- **Tipagem**: Com Pydantic, oferece validação e parsing automático de dados.
- **Assíncrono**: Perfeito para aplicações de grande escala e microserviços que requerem alta performance.
- **Documentação Automática**: Suporte nativo para Swagger e Redoc.

Agora minha stack de desenvolvimento de APIs inclui:
- **Flask** e **FastAPI** no **Python**
- **Express** no **Node.js**

---

## 🛠 **Tecnologias Utilizadas**

- **Linguagem**: Python 3.9+
- **Framework**: FastAPI
- **Princípios**: SOLID, DDD, DRY
- **Autenticação**: JWT (JSON Web Tokens)
- **Criptografia**: Assimétrica (RSA)
- **Banco de Dados**:
  - **SQLAlchemy** (Rede e Blockchain)
  - Bancos separados para dados tradicionais e tokenomics/blockchain.
- **Integração Blockchain**: Simulações de tokenomics.


![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.78.0-green.svg)
![SOLID](https://img.shields.io/badge/SOLID-Principles-yellow.svg)
![DDD](https://img.shields.io/badge/DDD-Domain--Driven--Design-orange.svg)
![JWT](https://img.shields.io/badge/JWT-Authentication-red.svg)
![Cryptography](https://img.shields.io/badge/Cryptography-Asymmetric%20Encryption-lightblue.svg)
![Blockchain](https://img.shields.io/badge/Blockchain-Network%20Integration-black.svg)

> Projeto de implementação de uma API RESTful utilizando **FastAPI**, **Domain-Driven Design (DDD)** e **princípios SOLID** para uma aplicação conceito de tokenomics, integrando criptografia assimétrica e autenticação com **JWT**.

![temp_image](https://github.com/user-attachments/assets/a448764f-ba3b-4b60-b2ee-4ac168c6c2d1)
![diagram-export-27-09-2024-13_18_22](https://github.com/user-attachments/assets/b74df88a-3a1e-4cf8-b7f3-d70a52f7645d)
![diagram-export-27-09-2024-13_21_15](https://github.com/user-attachments/assets/e4138539-6023-4779-9490-533e05ca1389)
![diagram-export-27-09-2024-13_26_58](https://github.com/user-attachments/assets/5a85c211-2d0b-4915-a002-96281e318d21)
![mintty_lJu9FZTzqH](https://github.com/user-attachments/assets/b5cbcebe-0699-4786-9956-df7b016d1896)
![Code_NEoXX62zwV](https://github.com/user-attachments/assets/3c008ca0-e03c-4832-9160-5e147707e62b)
![powershell_HB5ozvK4vT](https://github.com/user-attachments/assets/045cfcc2-5da8-4d8e-96b1-7dcbcb8b5bb6)
![powershell_9I75J48D6W](https://github.com/user-attachments/assets/0d9ad692-7eb1-45d5-92fb-e2c650c4455f)

---

## 📝 **Descrição do Projeto**

Este projeto foi criado para consolidar meus conhecimentos em **Python** e **FastAPI**, onde venho de um background de **Flask** desde 2018 e agora estou ampliando minha stack para incluir **FastAPI**. Escolhi FastAPI devido à sua performance superior, tipagem moderna com Pydantic, e compatibilidade com sistemas assíncronos, tornando-a ideal para **microserviços** de alta escala.

A API foi construída seguindo os princípios de **DDD (Domain-Driven Design)** e **SOLID**, com um foco forte em **DRY** (Don't Repeat Yourself) para garantir um código modular e sustentável.

# 🚀 FastAPI-Tokenomics-RESTful-API

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.78.0-green.svg)
![SOLID](https://img.shields.io/badge/SOLID-Principles-yellow.svg)
![DDD](https://img.shields.io/badge/DDD-Domain--Driven--Design-orange.svg)
![JWT](https://img.shields.io/badge/JWT-Authentication-red.svg)
![Cryptography](https://img.shields.io/badge/Cryptography-Asymmetric%20Encryption-lightblue.svg)
![Blockchain](https://img.shields.io/badge/Blockchain-Network%20Integration-black.svg)

> Projeto de implementação de uma API RESTful utilizando **FastAPI**, **Domain-Driven Design (DDD)** e **princípios SOLID** para uma aplicação conceito de tokenomics, integrando criptografia assimétrica e autenticação com **JWT**.

---


---

## 🌳 **Arquitetura do Projeto**

O projeto foi desenvolvido com **Domain-Driven Design (DDD)** e é totalmente modularizado. As camadas seguem uma divisão clara entre:
1. **Camada de Domínio**: Definições das entidades, regras de negócio e agregados.
2. **Camada de Aplicação**: Serviços e handlers que coordenam as requisições.
3. **Camada de Infraestrutura**: Integração com bancos de dados e outros serviços externos.


---

## 🧩 **Princípios SOLID Aplicados**

- **Single Responsibility Principle**: Cada módulo da aplicação possui uma única responsabilidade, facilitando manutenção e escalabilidade.
- **Open/Closed Principle**: A aplicação está aberta para extensão, mas fechada para modificação direta, garantindo que novas features sejam adicionadas sem comprometer o funcionamento existente.
- **Liskov Substitution Principle**: Todas as classes podem ser substituídas por suas subclasses sem afetar o comportamento do sistema.
- **Interface Segregation Principle**: Interfaces pequenas e específicas são criadas para cada caso de uso.
- **Dependency Inversion Principle**: A camada de aplicação depende de abstrações (interfaces) em vez de implementações concretas.

---

## 🔑 **Autenticação e Segurança**

O projeto utiliza **JWT** para autenticação de usuários, com suporte para tokens de acesso e refresh. A segurança é complementada com:
- **Criptografia Assimétrica (RSA)**: Utilizada para proteger tokens e dados sensíveis.
  
---

## 🏦 **Banco de Dados e Blockchain**

A arquitetura do banco de dados é dividida em dois segmentos:
1. **Banco Relacional (SQLAlchemy)**: Usado para gerenciar dados da rede.
2. **Blockchain Tokenomics**: Simulações de transferência de tokens e contratos inteligentes, permitindo verificar integrações e visualizações futuras.

Print da arquitetura do banco de dados:  

---

## 🧪 **Testes e Cobertura**

O projeto foi desenvolvido com foco em testes unitários e integração. A cobertura inclui:
- Testes de autenticação JWT.
- Verificação de criptografia.
- Validação de contratos de blockchain.

---

## 📂 **Estrutura de Pastas**


### ⚡ Por que **FastAPI**?

- **Performance**: FastAPI é extremamente rápida, comparável a Node.js e Go.
- **Tipagem**: Com Pydantic, oferece validação e parsing automático de dados.
- **Assíncrono**: Perfeito para aplicações de grande escala e microserviços que requerem alta performance.
- **Documentação Automática**: Suporte nativo para Swagger e Redoc.

Agora minha stack de desenvolvimento de APIs inclui:
- **Flask** e **FastAPI** no **Python**
- **Express** no **Node.js**

---

## 🛠 **Tecnologias Utilizadas**

- **Linguagem**: Python 3.9+
- **Framework**: FastAPI
- **Princípios**: SOLID, DDD, DRY
- **Autenticação**: JWT (JSON Web Tokens)
- **Criptografia**: Assimétrica (RSA)
- **Banco de Dados**:
  - **SQLAlchemy** (Rede e Blockchain)
  - Bancos separados para dados tradicionais e tokenomics/blockchain.
- **Integração Blockchain**: Simulações de tokenomics.

---

## 🌳 **Arquitetura do Projeto**

O projeto foi desenvolvido com **Domain-Driven Design (DDD)** e é totalmente modularizado. As camadas seguem uma divisão clara entre:
1. **Camada de Domínio**: Definições das entidades, regras de negócio e agregados.
2. **Camada de Aplicação**: Serviços e handlers que coordenam as requisições.
3. **Camada de Infraestrutura**: Integração com bancos de dados e outros serviços externos.


---

## 🧩 **Princípios SOLID Aplicados**

- **Single Responsibility Principle**: Cada módulo da aplicação possui uma única responsabilidade, facilitando manutenção e escalabilidade.
- **Open/Closed Principle**: A aplicação está aberta para extensão, mas fechada para modificação direta, garantindo que novas features sejam adicionadas sem comprometer o funcionamento existente.
- **Liskov Substitution Principle**: Todas as classes podem ser substituídas por suas subclasses sem afetar o comportamento do sistema.
- **Interface Segregation Principle**: Interfaces pequenas e específicas são criadas para cada caso de uso.
- **Dependency Inversion Principle**: A camada de aplicação depende de abstrações (interfaces) em vez de implementações concretas.

---

## 🔑 **Autenticação e Segurança**

O projeto utiliza **JWT** para autenticação de usuários, com suporte para tokens de acesso e refresh. A segurança é complementada com:
- **Criptografia Assimétrica (RSA)**: Utilizada para proteger tokens e dados sensíveis.
  
---

## 🏦 **Banco de Dados e Blockchain**

A arquitetura do banco de dados é dividida em dois segmentos:
1. **Banco Relacional (SQLAlchemy)**: Usado para gerenciar dados da rede.
2. **Blockchain Tokenomics**: Simulações de transferência de tokens e contratos inteligentes, permitindo verificar integrações e visualizações futuras.

Print da arquitetura do banco de dados:  

---

## 🧪 **Testes e Cobertura**

O projeto foi desenvolvido com foco em testes unitários e integração. A cobertura inclui:
- Testes de autenticação JWT.
- Verificação de criptografia.
- Validação de contratos de blockchain.

---

## 📂 **Estrutura de Pastas**

