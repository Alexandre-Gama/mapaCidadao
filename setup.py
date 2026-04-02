import re
import secrets
import sys
from pathlib import Path

if Path('.env').exists():
    print('.env ja existe. Remova-o manualmente para recriar.')
    sys.exit(1)

content = Path('.env.example').read_text()
content = re.sub(r'DJANGO_SECRET_KEY=.*', 'DJANGO_SECRET_KEY=' + secrets.token_urlsafe(50), content)
content = re.sub(r'DB_PASSWORD=.*', 'DB_PASSWORD=' + secrets.token_urlsafe(32), content)
Path('.env').write_text(content)

print('.env criado com sucesso.')
