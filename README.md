# Mini RAG Platform

A small production-style Retrieval-Augmented Generation (RAG) service built with Python, FastAPI, PostgreSQL, and pgvector.

## Goal

Build a minimal but solid RAG system that demonstrates:

- clean Python architecture
- FastAPI backend design
- vector search with PostgreSQL + pgvector
- testing and quality practices
- Docker-based local setup
- readiness for AWS deployment

## Use Case

Technical Documentation Assistant

The system ingests technical documents and allows users to query them, returning grounded answers with cited sources.

## Planned Stack

- Python 3.11+
- FastAPI
- PostgreSQL
- pgvector
- pytest
- Docker
- GitHub Actions
- AWS (ECS, RDS)
- Streamlit (demo UI)

## Project Structure (planned)

```

app/
tests/

````

## Development Setup (initial)

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
````

## Roadmap (high level)

* [ ] Project setup
* [ ] Core RAG domain (chunking, retrieval)
* [ ] PostgreSQL + pgvector integration
* [ ] FastAPI endpoints
* [ ] Basic frontend demo (Streamlit)
* [ ] Testing (unit + API)
* [ ] Docker setup
* [ ] CI with GitHub Actions
* [ ] AWS deployment

## Status

Project initialization in progress.