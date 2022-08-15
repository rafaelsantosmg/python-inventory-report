import json
from .importer import Importer


class JsonImporter(Importer):
    def import_data(file_path):
        if ".json" not in file_path:
            raise ValueError("Arquivo inválido")

        with open(file_path) as file:
            inventory_reader = list(json.load(file))
            return inventory_reader
