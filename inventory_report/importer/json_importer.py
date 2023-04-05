from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith('.json'):
            raise ValueError('Arquivo inválido')
        else:
            with open(path) as file:
                data = file.read()
                return json.loads(data)
