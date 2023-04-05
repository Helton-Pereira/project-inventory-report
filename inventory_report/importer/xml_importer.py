from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith('.xml'):
            raise ValueError('Arquivo inválido')
        else:
            with open(path) as file:
                data = file.read()
                return [row for row in xmltodict.parse(
                    data)['dataset']['record']]
