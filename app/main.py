from fastapi import FastAPI
import os
import psutil
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

app = FastAPI()

# Prometheus metrics
cpu_gauge = Gauge("app_cpu_percent", "CPU usage percentage")
mem_gauge = Gauge("app_memory_percent", "Memory usage percentage")

# Environment-configurable settings
APP_NAME = os.getenv("APP_NAME", "DevOps Demo")
VERSION = os.getenv("APP_VERSION", "1.0.0")

@app.get("/")
def root():
    return {"status": "ok", "message": "Hello from DevOps Demo!"}

@app.get("/health")
def health_check():
    return {"health": "pass"}

@app.get("/metrics")
def metrics():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    cpu_gauge.set(cpu)
    mem_gauge.set(mem)
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/info")
def info():
    return {"app": APP_NAME, "version": VERSION}