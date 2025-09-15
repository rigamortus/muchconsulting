ARG VERSION=3.11-slim
FROM python:${VERSION}

WORKDIR /app

COPY app/requirements.txt .
RUN pip install -r requirements.txt

COPY app/ .

USER 1000
ARG timezone=Africa/Lagos
ENV TZ=$timezone
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]