#Importa o FastAPI Router (usado para criar rotas separadas)
from fastapi import APIRouter

#Importa o modelo de dados (Pydantic)
from backend.models.transaction import Transaction

#Importa a função de negócio (service)
from backend.services.fraud_service import analyze_transaction

#Cria um roteador específico para previsões
router = APIRouter()

#Define um endpoint POST chamado /predict
@router.post("/predict")
def predict(transaction: Transaction):
    """
    Endpoint responsável por receber uma transação
    e retornar se ela é suspeita de fraude
    """

    #Chama a lógica de negócio passando os dados validados
    result = analyze_transaction(transaction)

    #Retorna o resultado para o cliente
    return result


