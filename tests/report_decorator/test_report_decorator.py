from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport

mock = [
    {
        "id": 1,
        "nome_do_produto": "MESA",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2022-05-04",
        "data_de_validade": "2022-09-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
    },
    {
        "id": 1,
        "nome_do_produto": "MESA",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2021-05-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
    },
    {
        "id": 2,
        "nome_do_produto": "MESA2",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2022-05-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
    },
    {
        "id": 3,
        "nome_do_produto": "MESA3",
        "nome_da_empresa": "Forces",
        "data_de_fabricacao": "2022-05-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
    },
]


AZUL = "\033[36m"
VERDE = "\033[32m"
VERMELHO = "\033[31m"
FIM = "\033[0m"
data_de_fabricacao = "2021-05-04"
data_de_validade = "2022-09-09"
nome_empresa = "Forces of Nature"


def test_decorar_relatorio():
    report_colorido = ColoredReport(SimpleReport).generate(mock)
    report_esperado = (
        f"{VERDE}Data de fabricação mais antiga:{FIM} "
        f"{AZUL}{data_de_fabricacao}{FIM}\n"
        f"{VERDE}Data de validade mais próxima:{FIM} "
        f"{AZUL}{data_de_validade}{FIM}\n"
        f"{VERDE}Empresa com mais produtos:{FIM} "
        f"{VERMELHO}{nome_empresa}{FIM}"
    )

    assert report_colorido == report_esperado
