# Mapa Cidadão

Plataforma para registro e visualização de denúncias de problemas urbanos.

## Requisitos

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Configuração do ambiente

### 1. Gerar credenciais

**Django Secret Key:**
```sh
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

**Senha do PostgreSQL:**
```sh
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### 2. Criar o arquivo `.env`

```sh
cp .env.example .env
```

Edite o `.env` preenchendo os valores gerados acima:

```env
DJANGO_SECRET_KEY=<resultado do primeiro comando>
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=mapacidadao
DB_USER=mapacidadao
DB_PASSWORD=<resultado do segundo comando>
DB_HOST=db
DB_PORT=5432
```

### 3. Subir o ambiente

```sh
docker compose up --build
```

A aplicação estará disponível em **http://localhost:8080**.

## Estrutura dos containers

| Container | Imagem | Função |
|---|---|---|
| `db` | postgres:16-alpine | Banco de dados PostgreSQL |
| `web` | (build local) | Aplicação Django via Gunicorn |
| `nginx` | nginx:1.27-alpine | Servidor web / proxy reverso |

## Parar o ambiente

```sh
# Parar sem remover dados
docker compose down

# Parar e remover todos os dados (banco, estáticos, mídia)
docker compose down -v
```
