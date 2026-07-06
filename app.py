from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "online", "mensaje": "Desplegado con GitHub Actions y ArgoCD en AWS v1.0.7"}