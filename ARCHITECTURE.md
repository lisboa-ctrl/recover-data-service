# Arquitetura do Projeto

Este projeto segue uma arquitetura em **3 camadas** simples e organizada:

## 📁 Estrutura de Pastas

```
app/
├── controllers/              # CAMADA 1: Controllers (API)
│   ├── health_controller.py  # Endpoint de health check
│   └── report_controller.py  # Endpoints de relatórios
│
├── domain/                   # CAMADA 2: Domínio
│   ├── entities/             # Entidades de negócio
│   ├── schemas/              # DTOs/Schemas Pydantic
│   │   └── report_schema.py
│   └── services/             # Serviços de domínio
│       └── pdf_generator.py
│
├── infrastructure/           # CAMADA 3: Infraestrutura
│   ├── config/               # Configurações
│   │   └── settings.py
│   ├── database/             # Banco de dados
│   │   ├── connection.py
│   │   ├── models/           # Modelos SQLAlchemy
│   │   │   └── base.py
│   │   └── repositories/     # Repositórios (acesso a dados)
│   └── templates/            # Templates HTML
│       └── base_report.html
│
└── main.py                   # Entry point da aplicação
```

## 🎯 Responsabilidades das Camadas

### 1️⃣ Controllers (Camada de Apresentação)
**Localização:** `app/controllers/`

**Responsabilidades:**
- Receber requisições HTTP
- Validar entrada via schemas
- Chamar serviços de domínio
- Retornar responses HTTP formatadas
- Definir rotas e endpoints da API

**Exemplo:**
```python
from app.controllers import health_router, report_router
```

### 2️⃣ Domain (Camada de Negócio)
**Localização:** `app/domain/`

**Responsabilidades:**
- **Entities:** Representar conceitos de negócio puros
- **Schemas:** Validação e serialização de dados (DTOs)
- **Services:** Implementar lógica de negócio (geração de PDF, processamento de dados)

**Exemplo:**
```python
from app.domain.schemas import DateRangeRequest
from app.domain.services import generate_pdf, render_report_html
```

### 3️⃣ Infrastructure (Camada de Infraestrutura)
**Localização:** `app/infrastructure/`

**Responsabilidades:**
- **Config:** Gerenciar configurações e variáveis de ambiente
- **Database:** Conexões, modelos ORM, repositórios de dados
- **Templates:** Recursos externos (HTML, arquivos estáticos)

**Exemplo:**
```python
from app.infrastructure.config import settings
from app.infrastructure.database import check_db_connection
```

## 🔄 Fluxo de Dados

```
HTTP Request
    ↓
Controllers (valida entrada)
    ↓
Domain Services (processa lógica de negócio)
    ↓
Infrastructure (acessa banco/recursos)
    ↓
Controllers (formata resposta)
    ↓
HTTP Response
```

## ✅ Benefícios desta Arquitetura

1. **Separação Clara:** Cada camada tem responsabilidades bem definidas
2. **Testabilidade:** Camadas podem ser testadas isoladamente
3. **Manutenibilidade:** Fácil localizar e modificar código
4. **Escalabilidade:** Simples adicionar novos recursos
5. **Clean Architecture:** Domínio independente de infraestrutura
6. **Baixo Acoplamento:** Mudanças em uma camada não afetam as outras

## 🚀 Como Adicionar Novas Features

### Adicionar novo endpoint:
1. Criar controller em `controllers/`
2. Criar schema em `domain/schemas/`
3. Implementar service em `domain/services/`
4. Registrar router no `main.py`

### Adicionar novo repositório:
1. Criar model em `infrastructure/database/models/`
2. Criar repository em `infrastructure/database/repositories/`
3. Usar repository nos services do domínio

### Adicionar nova configuração:
1. Adicionar variável em `infrastructure/config/settings.py`
2. Documentar no `.env.example`
