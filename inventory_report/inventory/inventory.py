import csv
import json
from xml.etree import ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_csv(file_path):
        with open(file_path, encoding="utf8") as file:
            inventory_reader = list(csv.DictReader(file))
        return inventory_reader

    def import_json(file_path):
        with open(file_path) as file:
            inventory_reader = list(json.load(file))
        return inventory_reader

    def import_xml(file_path):
        tree = ET.parse(file_path)
        root = list(tree.getroot())
        dict_list = list()
        for index in range(len(root)):
            info_dict = dict()
            for info in root[index]:
                info_dict[info.tag] = info.text
            dict_list.append(info_dict)
        return dict_list

    def select_file(file_path):
        if "csv" in file_path:
            return Inventory.import_csv(file_path)
        elif "json" in file_path:
            return Inventory.import_json(file_path)
        elif "xml" in file_path:
            return Inventory.import_xml(file_path)

    def import_data(file_path, strategy):
        inventory_list = Inventory.select_file(file_path)

        if strategy == "simples":
            return SimpleReport.generate(inventory_list)

        if strategy == "completo":
            return CompleteReport.generate(inventory_list)
