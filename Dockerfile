FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# COPY app ./app

COPY . .

# Make the Vault wait script executable
RUN chmod +x wait_for_vault.sh

ENTRYPOINT ["./wait-for-vault.sh"]

# CMD ["gunicorn", "app.main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
