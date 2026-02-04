# Importa a função de estatística
from backend.services.statistics_service import get_customer_statistics

# Testa para o cliente 101
stats = get_customer_statistics(101)

# Imprime o resultado no terminal
print(stats)
