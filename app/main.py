from fastapi import FastAPI

app = FastAPI(title="Ask Your Data", version="0.1.0")

@app.get("/health")
def health() -> dict:
    """Liveness check used by Docker, CI, and later Kubernetes probes."""
    return {"status": "fine"}