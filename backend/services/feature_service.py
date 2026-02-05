# Importa o modelo Transaction para tipagem
from backend.models.transaction import Transaction

# Importta estatística do cliente
from backend.services.statistics_service import get_customer_statistics

def extract_features(transaction: Transaction):
        """
        Extrai features numéricas a partir de uma transação
        e do histórico do cliente.
        """

        # Busca estatísticas do cliente
        stats = get_customer_statistics(transaction.customer_id)

        # Inicializa dicionário de features
        features = {}

        # Feature 1: valor da transação
        features["amount"] = transaction.amount

        # Feature 2: transação online (0 ou 1)
        features["is_online"] = int(transaction.is_online)

        # Feature 3: quantidade de transações do cliente
        features["total_transactions"] = stats["total_transactions"]

        # Feature 4: diferença para a média
        features["diff_from_mean"] = transaction.amount - stats["mean_amount"]

        # Feature 5: diferença para a mediana
        features["diff_from_median"] = transaction.amount - stats["median_amount"]

        # Feature 6: acima do limite IQR (0 ou 1)
        upper_iqr_limit = stats["q3"] + (1.5 * stats["iqr"])
        features["above_iqr_limit"] = int(transaction.amount > upper_iqr_limit)

        # Feature 7: valor absoluto alto (0 ou 1)
        features["very_high_amount"] = int(transaction.amount > 4000)

        return features

