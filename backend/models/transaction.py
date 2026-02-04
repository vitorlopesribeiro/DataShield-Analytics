# Importa BaseModel do Pydantic para criar modelos de dados
from pydantic import BaseModel


# Classe que representa uma transação de cartão
class Transaction(BaseModel):

    # ID do cliente
    customer_id: int

    # Valor da transação
    amount: float

    # Se a transação foi online
    is_online: bool
