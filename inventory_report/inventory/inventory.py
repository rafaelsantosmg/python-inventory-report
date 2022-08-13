import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_data(file_path, strategy):
        inventory_list = list()
        with open(file_path, encoding="utf8") as file:
            inventory_reader = csv.DictReader(file)
            for row in inventory_reader:
                inventory_list.append(dict(row))

        if strategy == "simples":
            return SimpleReport.generate(inventory_list)

        if strategy == "completo":
            return CompleteReport.generate(inventory_list)
