from fastapi import FastAPI

app = FastAPI(
    title="PlataformaCobranca API",
    description="Microsserviço de Gestão de Cobranças e Pagamentos",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"mensagem": "API da PlataformaCobranca em execução!"}

@app.get("/health")
def health_check():
    # Rota simples para verificar o status do serviço
    return {"status": "ok"}