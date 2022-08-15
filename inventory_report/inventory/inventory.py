from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from ..importer.csv_importer import CsvImporter
from ..importer.json_importer import JsonImporter
from ..importer.xml_importer import XmlImporter


class Inventory:
    def select_file(file_path):
        if "csv" in file_path:
            return CsvImporter.import_data(file_path)
        elif "json" in file_path:
            return JsonImporter.import_data(file_path)
        elif "xml" in file_path:
            return XmlImporter.import_data(file_path)

    def import_data(file_path, strategy):
        inventory_list = Inventory.select_file(file_path)

        if strategy == "simples":
            return SimpleReport.generate(inventory_list)

        if strategy == "completo":
            return CompleteReport.generate(inventory_list)
