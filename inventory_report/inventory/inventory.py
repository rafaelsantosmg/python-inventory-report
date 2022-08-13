import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_csv(file_path):
        inventory_list = list()
        with open(file_path, encoding="utf8") as file:
            inventory_reader = csv.DictReader(file)
            for row in inventory_reader:
                inventory_list.append(dict(row))
        return inventory_list

    def import_json(file_path):
        inventory_list = list()
        with open(file_path) as file:
            inventory_reader = json.load(file)
            print(inventory_reader)
            for row in inventory_reader:
                inventory_list.append(dict(row))
        return inventory_list

    def import_data(file_path, strategy):
        inventory_list = list()
        if "csv" in file_path:
            inventory_list = Inventory.import_csv(file_path)
        elif "json" in file_path:
            inventory_list = Inventory.import_json(file_path)

        if strategy == "simples":
            return SimpleReport.generate(inventory_list)

        if strategy == "completo":
            return CompleteReport.generate(inventory_list)
