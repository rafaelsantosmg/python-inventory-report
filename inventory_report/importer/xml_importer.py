from xml.etree import ElementTree as ET
from .importer import Importer


class XmlImporter(Importer):
    def import_data(file_path):
        if ".xml" not in file_path:
            raise ValueError("Arquivo inválido")

        tree = ET.parse(file_path)
        root = list(tree.getroot())
        dict_list = list()
        for index in range(len(root)):
            info_dict = dict()
            for info in root[index]:
                info_dict[info.tag] = info.text
            dict_list.append(info_dict)
        return dict_list
