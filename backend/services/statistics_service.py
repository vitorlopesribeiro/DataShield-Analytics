# Importa a biblioteca pandas para análise de dados
import pandas as pd

def load_transactions():
    """
    Carrega o histórico de transações a partir de um arquivo CSV
    e retorna um DataFrame do Pandas.
    """

    # Lê o arquivo CSV localizado na pasta data
    df = pd.read_csv("data/transactions.csv")

    # Retorna o DataFrame carregado
    return df

def get_customer_statistics(customer_id: int):
    """
    Calcula estatísticas básicas de um cliente específico.
    """

    # Carrega todas as transações
    df = load_transactions()

    # Filtra apenas as transações do cliente informado
    customer_data = df[df["customer_id"] == customer_id]

    # Cliente sem histórico
    if customer_data.empty:
        return {
            "customer_id": customer_id,
            "mean_amount": 0,
            "std_amount": 0,
            "total_transactions": 0
        }

    # Extrai apenas os valores das transações
    amounts = customer_data["amount"]

    # Média dos valores das transaçõe
    mean_amount = amounts.mean()

    # Desvio padrão dos valores
    std_amount = amounts.std()

    # Estatísticas robustas
    median_amount = amounts.median()
    q1 = amounts.quantile(0.25)
    q3 = amounts.quantile(0.75)
    iqr = q3 - q1

    # Retorna as estatísticas calculadas
    return{
        "customer_id" : customer_id,
        "mean_amount" : mean_amount,
        "std_amount" : std_amount,
        "median_amount" : median_amount,
        "q1" : q1,
        "q3" : q3,
        "iqr" : iqr,
        "total_transactions" : len(customer_data)
    }