import pytest
from module.main import main

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


    # def test_init_product(product_apple):
    #     assert product_apple.name == "Apple"
    #     assert product_apple.description == "red"
    #     assert product_apple.price == 99.9
    #     assert product_apple.quantity == 1000
    #
    # def test_init_category(category_fruit):
    #     assert category_fruit.name == "fruits"
    #     assert category_fruit.description == "fruits from India"
    #     assert category_fruit.products == ["banana", "mango"]
    #     assert category_fruit.product_count == 2
    #     assert category.category_count == 1

    # "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    # assert main() == ("08.12.2019 Открытие вклада\nСчет **5907\n41096.24 USD\n\n"
    #                   "07.12.2019 Перевод организации\nVisa Classic 2842 87** **** 9012 -> Счет **3655\n48150.39 USD\n\n"
    #                   "19.11.2019 Перевод организации\nMaestro 7810 84** **** 5568 -> Счет **2869\n30153.72 руб.\n\n"
    #                   "13.11.2019 Перевод со счета на счет\nСчет **9794 -> Счет **8125\n62814.53 руб.\n\n"
    #                   "05.11.2019 Открытие вклада\nСчет **8381\n21344.35 руб.\n\n")
