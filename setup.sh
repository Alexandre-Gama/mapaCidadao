#!/bin/sh
set -e

if [ -f .env ]; then
    echo ".env já existe. Remova-o manualmente para recriar."
    exit 1
fi

SECRET_KEY=$(python3 -c "import secrets; print(secrets.token_urlsafe(50))")
DB_PASSWORD=$(python3 -c "import secrets; print(secrets.token_urlsafe(32))")

sed \
    -e "s|DJANGO_SECRET_KEY=.*|DJANGO_SECRET_KEY=${SECRET_KEY}|" \
    -e "s|DB_PASSWORD=.*|DB_PASSWORD=${DB_PASSWORD}|" \
    .env.example > .env

echo ".env criado com sucesso."
