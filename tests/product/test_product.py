from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        'Produto X',
        'Empresa Y',
        '25/12/2022',
        'Sem expiração',
        '123456',
        'em local seco')

    assert product.id == 1
    assert product.nome_do_produto == 'Produto X'
    assert product.nome_da_empresa == 'Empresa Y'
    assert product.data_de_fabricacao == '25/12/2022'
    assert product.data_de_validade == 'Sem expiração'
    assert product.numero_de_serie == '123456'
    assert product.instrucoes_de_armazenamento == 'em local seco'
