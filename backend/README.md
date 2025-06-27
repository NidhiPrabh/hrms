## Backend

Python 3.12 / FastAPI application.

### Local Dev (without Docker)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
alembic upgrade head     # create tables
uvicorn app.main:app --reload
```

Run tests:

```bash
pytest
```
