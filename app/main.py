from fastapi import FastAPI
from pydantic import BaseModel
from app.calculator import add, subtract, multiply, divide

app = FastAPI(title="Calculator API")

class CalculationRequest(BaseModel):
    a: float
    b: float
    operation: str


@app.get("/")
def home():
    return {"message": "FastAPI Calculator Running"}


@app.post("/calculate")
def calculate(request: CalculationRequest):
    a = request.a
    b = request.b
    operation = request.operation

    if operation == "add":
        result = add(a, b)
    elif operation == "subtract":
        result = subtract(a, b)
    elif operation == "multiply":
        result = multiply(a, b)
    elif operation == "divide":
        result = divide(a, b)
    else:
        return {"error": "Invalid operation"}

    return {
        "a": a,
        "b": b,
        "operation": operation,
        "result": result
    }