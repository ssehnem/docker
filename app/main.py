from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/square/{x}")
def square(x: int):
    return {"result": x + x}

@app.get("/double/{x}")
def double(x: int):
    return {"result": x * 2}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)