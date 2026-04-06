# Guia de Configuração do Ambiente

## ✅ Status da Configuração

- ✅ **uv instalado:** v0.11.3
- ✅ **Python 3.12.13** instalado pelo uv
- ⚠️  **Dependências:** Erro ao instalar no WSL1

## ⚠️ Problema Identificado: WSL1

O ambiente atual está rodando em **WSL1** (Windows Subsystem for Linux 1), que tem limitações conhecidas com operações de I/O intensivas.

### Erro Encontrado
```
Cannot allocate memory (os error 12)
```

Este erro ocorre quando o uv tenta copiar muitos arquivos durante a instalação de pacotes.

## 🔧 Soluções Recomendadas

### Opção 1: Atualizar para WSL2 (RECOMENDADO)

WSL2 resolve completamente este problema e oferece melhor performance.

**No PowerShell (como Administrador):**
```powershell
# Verificar distribuições instaladas
wsl --list --verbose

# Converter para WSL2
wsl --set-version Ubuntu 2

# Definir WSL2 como padrão
wsl --set-default-version 2
```

Depois de converter, volte ao terminal Linux e execute:
```bash
export PATH="$HOME/.local/bin:$PATH"
cd /home/lisbuenothekid/dev/recover-data-service
uv sync
```

### Opção 2: Usar Docker

O projeto já tem suporte a Docker. Use o Dockerfile incluído:

```bash
# Construir imagem
docker build -t recover-data-service .

# Rodar container
docker run --env-file .env -p 8001:8001 recover-data-service
```

### Opção 3: Instalar em Ambiente Linux Nativo

Se tiver acesso a uma máquina Linux nativa ou VM com Linux:

```bash
# Instalar uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Instalar dependências
export PATH="$HOME/.local/bin:$PATH"
cd /path/to/recover-data-service
uv sync
```

### Opção 4: Usar Python Virtual Environment Tradicional

Como fallback, você pode usar venv + pip:

```bash
# Verificar se Python 3.12+ está disponível
python3 --version

# Se não, instalar Python 3.12+
sudo apt update
sudo apt install python3.12 python3.12-venv python3-pip

# Criar ambiente virtual
python3.12 -m venv .venv
source .venv/bin/activate

# Instalar dependências
pip install --upgrade pip
pip install -r requirements.txt  # (você precisará criar este arquivo)
```

**Criar requirements.txt:**
```txt
fastapi[standard]>=0.135.3
asyncpg>=0.31.0
jinja2>=3.1.6
pydantic-settings>=2.13.1
python-dotenv>=1.2.2
sqlalchemy[asyncio]>=2.0.49
weasyprint>=68.1
```

## 🚀 Verificar Instalação

Após resolver o problema e instalar as dependências:

```bash
export PATH="$HOME/.local/bin:$PATH"

# Testar imports
uv run python -c "from app.main import app; print('✓ Imports OK!')"

# Rodar servidor de desenvolvimento
uv run fastapi dev app/main.py --port 8001
```

## 📋 Comandos Úteis

### Com uv (após resolver problema de instalação)
```bash
# Sincronizar dependências
uv sync

# Rodar servidor
uv run fastapi dev app/main.py --port 8001

# Rodar testes
uv run pytest

# Adicionar nova dependência
uv add nome-do-pacote
```

### Verificar status
```bash
# Versão do uv
uv --version

# Python do projeto
uv run python --version

# Listar pacotes instalados
uv pip list
```

## 🔍 Debug

### Verificar WSL version
```bash
cat /proc/version
# ou no Windows PowerShell:
# wsl --list --verbose
```

### Verificar memória disponível
```bash
free -h
```

### Limpar cache do uv
```bash
uv cache clean
```

### Remover ambiente virtual e recomeçar
```bash
rm -rf .venv
uv sync
```

## 📚 Referências

- [Documentação do uv](https://docs.astral.sh/uv/)
- [WSL2 Installation Guide](https://learn.microsoft.com/en-us/windows/wsl/install)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
