from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, OutaTime!"}


# This is an amazing FastAPI application that serves as a starting point for your project.

