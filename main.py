from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Calculator API is running"}

@app.get("/add")
def add(a: float, b: float):
    return { a + b}

@app.get("/sub")
def sub(a: float, b: float):
    return { a - b}

@app.get("/mul")
def mul(a: float, b: float):
    return { a * b}

@app.get("/div")
def div(a: float, b: float):
    if b == 0:
        return {"error": "division by zero"}
    return { a / b}
