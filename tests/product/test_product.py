from inventory_report.inventory.product import Product
from ..factories.product_factory import ProductFactory


def test_cria_produto():
    productFake = ProductFactory()
    product = Product(
        productFake.id,
        productFake.nome_do_produto,
        productFake.nome_da_empresa,
        productFake.data_de_fabricacao,
        productFake.data_de_validade,
        productFake.numero_de_serie,
        productFake.instrucoes_de_armazenamento,
    )
    assert product.id == productFake.id
    assert product.nome_do_produto == productFake.nome_do_produto
    assert product.nome_da_empresa == productFake.nome_da_empresa
    assert product.data_de_fabricacao == productFake.data_de_fabricacao
    assert product.data_de_validade == productFake.data_de_validade
    assert product.numero_de_serie == productFake.numero_de_serie
    assert (
        product.instrucoes_de_armazenamento
        == productFake.instrucoes_de_armazenamento
    )
