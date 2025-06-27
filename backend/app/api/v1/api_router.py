from fastapi import APIRouter

from .endpoints import departments, employees, leaves, login, users

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, tags=["users"], prefix="/users")
api_router.include_router(departments.router, tags=["departments"], prefix="/departments")
api_router.include_router(employees.router, tags=["employees"], prefix="/employees")
api_router.include_router(leaves.router, tags=["leaves"], prefix="/leaves")
