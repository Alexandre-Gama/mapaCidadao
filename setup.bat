@echo off
setlocal

if exist .env (
    echo .env ja existe. Remova-o manualmente para recriar.
    exit /b 1
)

python -c "
import secrets, re

with open('.env.example') as f:
    content = f.read()

content = re.sub(r'DJANGO_SECRET_KEY=.*', 'DJANGO_SECRET_KEY=' + secrets.token_urlsafe(50), content)
content = re.sub(r'DB_PASSWORD=.*', 'DB_PASSWORD=' + secrets.token_urlsafe(32), content)

with open('.env', 'w') as f:
    f.write(content)

print('.env criado com sucesso.')
"
