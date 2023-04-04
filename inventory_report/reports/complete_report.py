from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def get_products_in_stock_by_company(list_of_products):
        all_companies = [
            product['nome_da_empresa'] for product in list_of_products
        ]
        companies_and_frequency = Counter(all_companies)
        companies_and_products_quantity = companies_and_frequency.most_common()
        final_list = ''
        for company in companies_and_products_quantity:
            name, amount = company
            final_list += f'- {name}: {amount}\n'
        return final_list

    @staticmethod
    def generate(list_of_products):
        oldest_date = SimpleReport.get_oldest_fabrication_date(
            list_of_products)
        nearest_expiration_date = SimpleReport.get_nearest_expiration_date(
            list_of_products)
        most_frequent_company = SimpleReport.get_most_frequent_company(
            list_of_products)
        products_in_stock = CompleteReport.get_products_in_stock_by_company(
            list_of_products
        )

        return (
            f'Data de fabricação mais antiga: {oldest_date}\n'
            f'Data de validade mais próxima: {nearest_expiration_date}\n'
            f'Empresa com mais produtos: {most_frequent_company}\n'
            'Produtos estocados por empresa:\n'
            f'{products_in_stock}\n'
        )
