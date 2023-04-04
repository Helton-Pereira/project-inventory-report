from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def get_oldest_fabrication_date(list_of_products):
        all_fabrication_dates = [
            product['data_de_fabricacao'] for product in list_of_products
        ]
        oldest_date = min(all_fabrication_dates)
        return oldest_date

    @staticmethod
    def get_nearest_expiration_date(list_of_products):
        today = datetime.today().strftime('%Y-%m-%d')
        all_expiration_dates = [
            product['data_de_validade'] for product in list_of_products
            if product['data_de_validade'] >= today
        ]
        nearest_expiration_date = min(all_expiration_dates)
        return nearest_expiration_date

    @staticmethod
    def get_most_frequent_company(list_of_products):
        all_companies = [
            product['nome_da_empresa'] for product in list_of_products
        ]
        companies_and_frequency = Counter(all_companies)
        most_frequent_company = companies_and_frequency.most_common(1)[0][0]
        return most_frequent_company

    @staticmethod
    def generate(list_of_products):
        oldest_date = SimpleReport.get_oldest_fabrication_date(
            list_of_products)
        nearest_expiration_date = SimpleReport.get_nearest_expiration_date(
            list_of_products)
        most_frequent_company = SimpleReport.get_most_frequent_company(
            list_of_products)

        return (
            f'Data de fabricação mais antiga: {oldest_date}\n'
            f'Data de validade mais próxima: {nearest_expiration_date}\n'
            f'Empresa com mais produtos: {most_frequent_company}'
        )
