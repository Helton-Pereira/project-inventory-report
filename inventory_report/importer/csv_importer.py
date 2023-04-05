from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith('.csv'):
            raise ValueError('Arquivo inválido')

        else:
            with open(path) as file:
                data = csv.DictReader(file)
                return [row for row in data]
