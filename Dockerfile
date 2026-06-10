FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/src

WORKDIR /app
COPY pyproject.toml README.md LICENSE ARCHITECTURE.md architecture.svg ./
COPY src ./src
COPY samples ./samples
COPY web ./web
COPY docs ./docs

EXPOSE 8000
CMD ["python", "-m", "prizepilot.webapp", "--host", "0.0.0.0", "--port", "8000"]
