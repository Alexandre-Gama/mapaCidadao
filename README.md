# Mapa Cidadão

Plataforma para registro e visualização de denúncias de problemas urbanos.

## Requisitos

- [Docker](https://docs.docker.com/get-docker/) (inclui Docker Compose)
- Python 3 (apenas para o script de setup)

## Instalação

### 1. Clonar o repositório

```sh
git clone <url-do-repositório>
cd mapaCidadao
```

### 2. Criar o arquivo `.env`

O script de setup gera automaticamente a `SECRET_KEY` do Django e a senha do PostgreSQL com valores aleatórios seguros.

**Linux / macOS:**
```sh
chmod +x setup.sh
./setup.sh
```

**Windows (PowerShell):**
```powershell
.\setup.ps1
```

> O script cria o `.env` a partir do `.env.example`, substituindo as credenciais por valores gerados automaticamente. Caso queira ajustar outras variáveis (como `DJANGO_ALLOWED_HOSTS`), edite o `.env` gerado antes de continuar.

### 3. Subir o ambiente

```sh
docker compose up --build
```

Na primeira execução, o Docker irá:
1. Construir a imagem da aplicação
2. Iniciar o banco de dados PostgreSQL
3. Executar as migrations automaticamente
4. Coletar os arquivos estáticos
5. Iniciar o Gunicorn e o Nginx

A aplicação estará disponível em **http://localhost:8080**.

## Variáveis de ambiente

| Variável | Descrição | Padrão |
|---|---|---|
| `DJANGO_SECRET_KEY` | Chave secreta do Django | — (obrigatória) |
| `DJANGO_DEBUG` | Ativa o modo debug | `False` |
| `DJANGO_ALLOWED_HOSTS` | Hosts permitidos, separados por vírgula | `localhost,127.0.0.1` |
| `DB_NAME` | Nome do banco de dados | `mapacidadao` |
| `DB_USER` | Usuário do banco de dados | `mapacidadao` |
| `DB_PASSWORD` | Senha do banco de dados | — (obrigatória) |
| `DB_HOST` | Host do banco de dados | `db` |
| `DB_PORT` | Porta do banco de dados | `5432` |

## Estrutura dos containers

| Container | Imagem | Função |
|---|---|---|
| `db` | postgres:16-alpine | Banco de dados PostgreSQL |
| `web` | (build local) | Aplicação Django via Gunicorn (porta 8000 interna) |
| `nginx` | nginx:1.27-alpine | Proxy reverso (porta 8080 → 80 → 8000) |

## Comandos úteis

```sh
# Parar sem remover dados
docker compose down

# Parar e remover todos os dados (banco, estáticos, mídia)
docker compose down -v

# Ver logs em tempo real
docker compose logs -f

# Acessar o shell da aplicação
docker compose exec web bash

# Criar superusuário Django
docker compose exec web python manage.py createsuperuser
```
