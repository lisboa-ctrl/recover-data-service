# recover-data-service

Microservice Python para geração de relatórios PDF conectado ao banco PostgreSQL do projeto [recover](https://github.com/kanoctrl/recover).

## Stack

- **Python 3.12**
- **FastAPI** — framework web
- **SQLAlchemy 2 + asyncpg** — acesso async ao PostgreSQL
- **WeasyPrint** — geração de PDF via HTML/CSS + Jinja2
- **uv** — gerenciador de pacotes

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
| `APP_ENV` | `development` | Ambiente da aplicação |
| `PORT` | `8001` | Porta do servidor |
