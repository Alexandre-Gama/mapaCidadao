if (Test-Path .env) {
    Write-Error ".env já existe. Remova-o manualmente para recriar."
    exit 1
}

$secretKey = python -c "import secrets; print(secrets.token_urlsafe(50))"
$dbPassword = python -c "import secrets; print(secrets.token_urlsafe(32))"

(Get-Content .env.example) `
    -replace 'DJANGO_SECRET_KEY=.*', "DJANGO_SECRET_KEY=$secretKey" `
    -replace 'DB_PASSWORD=.*', "DB_PASSWORD=$dbPassword" |
    Set-Content .env

Write-Host ".env criado com sucesso."
