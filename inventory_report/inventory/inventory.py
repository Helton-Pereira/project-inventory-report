from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


def read_files(path):
    with open(path) as file:
        if path.endswith('.csv'):
            data = csv.DictReader(file)
            return [row for row in data]
        elif path.endswith('.json'):
            data = file.read()
            return json.loads(data)
        elif path.endswith('.xml'):
            data = file.read()
            return [row for row in xmltodict.parse(data)['dataset']['record']]


class Inventory:
    @staticmethod
    def import_data(path, type):
        data = read_files(path)
        if type == 'simples':
            return SimpleReport.generate(data)
        elif type == 'completo':
            return CompleteReport.generate(data)
