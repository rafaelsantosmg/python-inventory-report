from inventory_report.inventory.product import Product
from ..factories.product_factory import ProductFactory


def test_relatorio_produto():
    productFake = ProductFactory()
    product = Product(
        productFake.id,
        productFake.nome_do_produto,
        productFake.nome_da_empresa,
        productFake.data_de_fabricacao,
        productFake.data_de_validade,
        productFake.numero_de_serie,
        productFake.instrucoes_de_armazenamento,
    ).__repr__()

    assert product == (
        f"O produto {productFake.nome_do_produto}"
        f" fabricado em {productFake.data_de_fabricacao}"
        f" por {productFake.nome_da_empresa} com validade"
        f" até {productFake.data_de_validade}"
        f" precisa ser armazenado {productFake.instrucoes_de_armazenamento}."
    )
