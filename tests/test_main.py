import pytest
from module.main import main

def test_main(product1, category1):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5

    assert category1.name == "Смартфоны"
    assert category1.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert type(category1.products) == list
    assert category1.category_count == 2
    assert category1.product_count == 2

# def test_product(product1):
#     assert product1.name == "Samsung Galaxy S23 Ultra"
#     assert product1.description == "256GB, Серый цвет, 200MP камера"
#     assert product1.price == 180000.0
#     assert product1.quantity == 5
#
# def test_category(category1):
#     assert category1.name == "Смартфоны"
#     assert category1.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
#     assert type(category1.products) == list
#     assert category1.category_count == 3
#     assert category1.product_count == 3