#!/bin/sh

echo "[backend] Waiting for Vault to become available..."

until curl -s "$VAULT_ADDR/v1/sys/health" | grep -q '"initialized":true'; do
  sleep 1
done

echo "[backend] Vault is up. Fetching secrets..."

export POSTGRES_USER=$(vault kv get -field=POSTGRES_USER secret/backend)
export POSTGRES_PASSWORD=$(vault kv get -field=POSTGRES_PASSWORD secret/backend)

echo "[backend] Secrets loaded. Starting app..."
exec gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
