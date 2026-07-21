from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Employee Directory API",
    version="1.0.0",
    description="A simple Employee Directory API used to learn DevOps from scratch."
)

# Temporary in-memory storage
employees = []


class Employee(BaseModel):
    id: int
    name: str
    department: str


@app.get("/")
def home():
    return {
        "message": "Welcome to Employee Directory API",
        "status": "Application is running successfully"
    }


@app.get("/health")
def health():
    return {"status": "UP"}


@app.get("/employees")
def get_employees():
    return employees


@app.post("/employees")
def create_employee(employee: Employee):
    employees.append(employee)
    return {
        "message": "Employee created successfully",
        "employee": employee
    }


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    global employees

    employees = [
        emp for emp in employees
        if emp.id != employee_id
    ]

    return {
        "message": f"Employee {employee_id} deleted successfully"
    }