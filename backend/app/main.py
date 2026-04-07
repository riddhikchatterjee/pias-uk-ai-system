from turtle import title
from fastapi import FastAPI

app = FastAPI(
    title = "PIAS-UK AI System",
    version = "1.0.0"
)

@app.get("/")
def root():
    return {"message" : "PIAS-UK system is running"}