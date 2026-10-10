
from fastapi import FastAPI

app = FastAPI(
    title="Minha primeira API",
    description="API de estudos em Python",
    version="1.0.0"
)

@app.get("/")
def inicio():
    return {
        "mensagem": "Minha API está funcionando!",
        "status": "Sucesso"
    }

@app.get("/sobre")
def sobre():
    return {
        "projeto": "Minha API",
        "linguagem": "Python",
        "framework": "FastAPI"
    }

@app.get("/sobre-mim")
def sobre_mim():
    return {
        "projeto": "Minha API",
        "linguagem": "Python",
        "framework": "FastAPI",
        "mensagem": "Meu projeto está no GitHub!"
    }