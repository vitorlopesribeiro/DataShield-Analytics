#Importa o modelo Transaction apenas para tipagem
from backend.models.transaction import Transaction

# Importa o serviço de estatísticas
from backend.services.feature_service import extract_features

def analyze_transaction(transaction: Transaction):
    """
    Analisa uma transação usando features extraídas
    """

    # Extrai as features da transação
    features = extract_features(transaction)

    # Inicializa score de risco
    risk_score = 0

    # Lista de motivos que explicam a decisão
    reasons = []

    # Regra 1: Pouco histórico
    if features["total_transactions"] < 5:
        risk_score += 2
        reasons.append("Customer has little transaction history")

    # Regra 2: Transação online
    if features["is_online"]:
        risk_score += 1
        reasons.append("Online transaction increases risk")

    # Regra 3: estatística robusta (IQR)
    if features["above_iqr_limit"]:
        risk_score += 3
        reasons.append("Transaction detected as outlier using IQR")

    # Regra 4: valor absoluto muito alto (regra de negócio)
    if features["very_high_amount"]:
        risk_score += 3
        reasons.append("Very high absolute transaction value")

    # Decisão final
    if risk_score >= 5:
        return {
            "fraud": True,
            "risk_score": risk_score,
            "reason": " | ".join(reasons),
            "feature_used" : features
        }

    return {
        "fraud": False,
        "risk_score": risk_score,
        "reason": " | ".join(reasons),
        "feature_used" : features
    }