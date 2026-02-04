#Importa o modelo Transaction apenas para tipagem
from backend.models.transaction import Transaction
from backend.services.statistics_service import get_customer_statistics

def analyze_transaction(transaction: Transaction):
    """
    Função responsável por analisar uma tranação
    e decidir se ela parece fraudulenta.
    """
    # Inicializa score de risco
    risk_score = 0

    #Busca estatísticas do cliente
    stats = get_customer_statistics(transaction.customer_id)

    mean_amount = stats["mean_amount"]
    std_amount = stats["std_amount"]
    total_transactions = stats["total_transactions"]

    # Feature 0: pouco histórico
    if total_transactions < 5:
        risk_score += 2

    # Feature 1: valor fora do padrão do cliente
    if total_transactions >= 5 and std_amount > 0:
        if transaction.amount > mean_amount + (2 * std_amount):
            risk_score += 3

    # Feature 2: valor absoluto alto
    if transaction.amount > 1000:
        risk_score += 2

    # Feature 3: transação online
    if transaction.is_online:
        risk_score += 1

    # Feature 4: combinação perigosa
    if transaction.amount > 1000 and transaction.is_online:
        risk_score += 2
    

    # Decisão final
    if risk_score >= 5:
        return {
            "fraud": True,
            "risk_score": risk_score,
            "reason": "Transaction classified as high risk using customer statistics"
        }
    # Caso contrário, considera normal
    return {
        "fraud": False,
        "risk_score": risk_score,
        "reason": "Transaction classified as low risk using customer statistics"
    }
    