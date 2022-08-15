import csv
from .importer import Importer


class CsvImporter(Importer):
    def import_data(file_path):
        if ".csv" not in file_path:
            raise ValueError("Arquivo inválido")

        with open(file_path, encoding="utf8") as file:
            inventory_reader = list(csv.DictReader(file))

        return inventory_reader
