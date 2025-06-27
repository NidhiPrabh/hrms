# Full‑Featured HRMS

A moderately complete Human Resource Management System (HRMS) with:

* **FastAPI** backend
* **SQLite** (dev) / **PostgreSQL** (prod via docker‑compose)
* JWT authentication
* CRUD APIs for Departments, Employees & Leave management
* Alembic migrations
* Basic test suite (pytest + httpx)
* Example React single‑page frontend

> ⚠️  This is a starter codebase for learning and PoC. Harden before production: add granular RBAC, proper logging, monitoring, rate limiting, validation, etc.

## Quick Start (All‑in‑one)

```bash
# clone, then:
cd backend
cp .env.example .env      # adjust secrets
docker compose up --build
```

API docs: `http://localhost:8000/docs`  
React UI: `http://localhost:3000`

---

See individual **backend/README.md** and **frontend/README.md** for details.
