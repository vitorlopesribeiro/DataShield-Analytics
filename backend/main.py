# Importa a classe FastAPI para criar a aplicação
from fastapi import FastAPI

# Importa o router de previsão
from backend.routers.predict import router as predict_router


# Cria a instância da aplicação FastAPI
app = FastAPI(
    title="DataShield Analytics",
    description="API para detecção de fraude em cartões",
    version="1.0.0"
)

# Registra o router na aplicação
app.include_router(predict_router)



