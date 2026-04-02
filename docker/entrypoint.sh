#!/bin/sh
set -e

echo "Aguardando o banco de dados..."
until python -c "
import os, psycopg2
psycopg2.connect(
    dbname=os.environ['DB_NAME'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD'],
    host=os.environ.get('DB_HOST', 'db'),
    port=os.environ.get('DB_PORT', '5432'),
)
" 2>/dev/null; do
  sleep 1
done
echo "Banco de dados disponível."

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec gunicorn MapaCidadaoProject.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --timeout 120
