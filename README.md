# Vane Enterprise Orchestrator Service

## Overview
A lightweight Python service providing structured fact-checking gates, configuration management, and API orchestration for the Vane Enterprise framework.

## Architecture
- **`app/config.py`**: Pydantic-backed environment configuration schema.
- **`app/orchestrator.py`**: Fact-checking gate and decision flow engine.
- **`app/logging_config.py`**: JSON-structured logging utility.

## Quick Start
```bash
# Clone & Install
pip install -r requirements-lock.txt

# Run Test Suite
pytest --cov=app --cov-fail-under=80
Docker Deployment 
```bash
docker-compose up --build

