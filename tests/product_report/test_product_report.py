from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        'Produto X',
        'Empresa Y',
        '25/12/2022',
        'Sem expiração',
        '123456',
        'em local seco')

    assert product.__repr__() == (
        'O produto Produto X fabricado em 25/12/2022 '
        'por Empresa Y com validade até Sem expiração '
        'precisa ser armazenado em local seco.')
