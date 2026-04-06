# recover-data-service

Microservice Python para geração de relatórios PDF conectado ao banco PostgreSQL do projeto [recover](https://github.com/kanoctrl/recover).

## Stack

- **Python 3.12**
- **FastAPI** — framework web
- **SQLAlchemy 2 + asyncpg** — acesso async ao PostgreSQL
- **WeasyPrint** — geração de PDF via HTML/CSS + Jinja2
- **uv** — gerenciador de pacotes

## Arquitetura

O projeto segue uma **arquitetura em 3 camadas** (Layered Architecture):

```
app/
├── controllers/         # CAMADA 1: API / Routers (HTTP)
├── domain/             # CAMADA 2: Lógica de Negócio
│   ├── entities/       # Entidades de domínio
│   ├── schemas/        # DTOs / Validação
│   └── services/       # Serviços de negócio
└── infrastructure/     # CAMADA 3: Recursos Externos
    ├── config/         # Configurações
    ├── database/       # PostgreSQL (models, repositories)
    └── templates/      # Templates HTML
```

📄 Para mais detalhes, consulte o arquivo [ARCHITECTURE.md](ARCHITECTURE.md)

## Setup

### Pré-requisitos

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- PostgreSQL do projeto `recover` rodando

### Instalação

```bash
cp .env.example .env
# edite .env com as credenciais do banco

uv sync
```

> ⚠️ **Nota WSL1:** Se você estiver usando WSL1 e encontrar erros como "Cannot allocate memory" durante `uv sync`, consulte o arquivo [SETUP.md](SETUP.md) para soluções alternativas. Recomendamos atualizar para WSL2.

### Rodar em desenvolvimento

```bash
uv run fastapi dev app/main.py --port 8001
```

### Rodar testes

```bash
uv run pytest
```

### Docker

```bash
docker build -t recover-data-service .
docker run --env-file .env -p 8001:8001 recover-data-service
```

## Endpoints

| Método | Path | Descrição |
|--------|------|-----------|
| `GET` | `/health` | Health check com status do banco |
| `POST` | `/api/v1/reports/pdf` | Gera PDF para o intervalo de datas |

### Exemplo de requisição

```bash
curl -X POST http://localhost:8001/api/v1/reports/pdf \
  -H "Content-Type: application/json" \
  -d '{"start_date": "2025-01-01", "end_date": "2025-03-31"}' \
  --output relatorio.pdf
```

## Variáveis de Ambiente

| Variável | Padrão | Descrição |
|----------|--------|-----------|
| `DATABASE_URL` | `postgresql+asyncpg://user:password@localhost:5432/recover` | URL de conexão com PostgreSQL |
| `APP_ENV` | `development` | Ambiente da aplicação (`development`, `uat`, `prd`) |
| `PORT` | `8001` | Porta do servidor |

## Ambientes

A aplicação carrega variáveis de ambiente com a seguinte prioridade (maior sobrescreve menor):

```
variáveis do OS  >  .env.{APP_ENV}  >  .env  >  defaults do código
```

### Development (padrão)

```bash
cp .env.example .env
# edite .env com as credenciais locais
uv run fastapi dev app/main.py --port 8001
```

### UAT

```bash
cp .env.uat.example .env.uat
# edite .env.uat com as credenciais de UAT
APP_ENV=uat uv run fastapi dev app/main.py --port 8001
```

### PRD — Docker com arquivo

```bash
cp .env.prd.example .env.prd
# edite .env.prd com as credenciais de produção
docker run --env APP_ENV=prd --env-file .env.prd -p 8001:8001 recover-data-service
```

### PRD — Docker com env vars injetadas (sem arquivo)

```bash
docker run \
  -e APP_ENV=prd \
  -e DATABASE_URL=postgresql+asyncpg://user:pass@prd-host:5432/recover \
  -p 8001:8001 \
  recover-data-service
```
