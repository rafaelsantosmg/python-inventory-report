from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(list):
        simple_report = SimpleReport.generate(list)
        empresas = Counter(
            prod["nome_da_empresa"]
            for prod in list
            if prod.get("nome_da_empresa")
        )
        complete_report = simple_report + "\nProdutos estocados por empresa:\n"
        for key, value in empresas.items():
            complete_report += f"- {key}: {value}\n"

        return complete_report
