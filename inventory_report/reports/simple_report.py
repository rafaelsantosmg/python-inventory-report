from datetime import datetime
from statistics import mode


class SimpleReport:
    def generate(list):
        antiga_data = sorted(list, key=lambda d: d["data_de_fabricacao"])[0][
            "data_de_fabricacao"
        ]
        produtos = sorted(list, key=lambda d: d["data_de_validade"])
        nome_empresa = mode(produto["nome_da_empresa"] for produto in list)
        data_atual = datetime.today().strftime("%Y-%m-%d")
        for produto in produtos:
            if produto["data_de_validade"] < data_atual:
                produtos.remove(produto)

        proxima_data = produtos[0]["data_de_validade"]

        return (
            f"Data de fabricação mais antiga: {antiga_data}\n"
            f"Data de validade mais próxima: {proxima_data}\n"
            f"Empresa com mais produtos: {nome_empresa}"
        )
