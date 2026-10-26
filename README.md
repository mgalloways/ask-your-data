# Ask Your Data

![CI](https://github.com/mgalloways/ask-your-data/actions/workflows/ci.yml/badge.svg)

An LLM-powered analytics app, built as a DevOps portfolio project.

## Run locally

    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    pip install -r requirements-dev.txt
    pytest
    uvicorn app.main:app --reload

## Run in Docker

    docker build -t ask-your-data .
    docker run -p 8000:8000 ask-your-data

## Security

Every push and pull request runs:
- Ruff (lint) and Bandit (static security scan)
- Pytest
- Trivy image scan, blocking HIGH and CRITICAL findings
- A container smoke test

Dependabot and GitHub secret scanning with push protection are enabled.