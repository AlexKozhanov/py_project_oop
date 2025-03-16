import pytest
from module.main import main

def test_main(product1, product2, product3, product4, category1, category2):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5

    assert product2.name == "Iphone 15"
    assert product2.description == "512GB, Gray space"
    assert product2.price == 210000.0
    assert product2.quantity == 8

    assert product3.name == "Xiaomi Redmi Note 11"
    assert product3.description == "1024GB, Синий"
    assert product3.price == 31000.0
    assert product3.quantity == 14

    assert product4.name == "55 QLED 4K"
    assert product4.description == "Фоновая подсветка"
    assert product4.price == 123000.0
    assert product4.quantity == 7

    assert category1.name == "Смартфоны"
    assert category1.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert type(category1.products) == list
    assert category1.category_count == 2
    assert category1.product_count == 3

    assert category2.name == "Телевизоры"
    assert category2.description == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    assert type(category2.products) == list
    assert category2.category_count == 2
    assert category2.product_count == 1
