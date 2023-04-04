from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    @staticmethod
    def import_data(path, type):
        list_dict = []
        if path[(len(path) - 1)] == 'v':
            with open(path, encoding='utf-8') as file:
                file_reader = csv.DictReader(file, delimiter=',')
                for product in file_reader:
                    list_dict.append(product)

        elif path[(len(path) - 1)] == 'n':
            with open(path, encoding='utf-8') as file:
                file_reader = json.load(file)
                for product in file_reader:
                    list_dict.append(product)

        if type == 'simples':
            return SimpleReport.generate(list_dict)
        elif type == 'completo':
            return CompleteReport.generate(list_dict)
