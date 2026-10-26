from fastapi import FastAPI

app = FastAPI(title="Ask Your Data", version="0.2.0")

@app.get("/health")
def health() -> dict:
    """Liveness check used by Docker, CI, and later Kubernetes probes."""
    return {"status": "ok"}

@app.get("/version")
def version() -> dict:
    """Report which version of the app is running."""
    return {"version": app.version}