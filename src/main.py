#INCLUDE:
from src.myerror import MyError
from src.function import read_json, pull_json, write_json
from src.category import Category
from src.product import Product, Smartphone, LawnGrass
import json

#DATA:
file_input = '../config/products.json'
file_output = '../config/output.json'

#INITIALIZATION.
def main(category1, category2, product1, product2, product3, product4):
    """Основная программа"""
    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)

if __name__ == "__main__":
    # Чтение данных из json
    list_Products, list_categories_1, list_categories_2 = read_json(file_input) # тут словари в списках

    # Распаковка данных из json
    category_1 = list_categories_1[0] # тут уже словари
    category_2 = list_categories_2[0]
    product_1 = list_Products[0]
    product_2 = list_Products[1]
    product_3 = list_Products[2]
    product_4 = list_Products[3]
    list_products_1 = [product_1, product_2, product_3]
    list_products_2 = [product_4]

    # Обработка данных в экземпляры класса
    category1 = Category.new_category(category_1, list_products_1)
    category2 = Category.new_category(category_2, list_products_2)
    product1 = Product.new_product(product_1)
    product2 = Product.new_product(product_2)
    product3 = Product.new_product(product_3)
    product4 = Product.new_product(product_4)

    # Основная программа
    main(category1, category2, product1, product2, product3, product4)

    # Кодировка данных в json
    # category_smartphones.products[3] = Product.decoder(category_smartphones.products[3])  # для кодировки в json
    category_list = []
    category_object = category1
    category_list = write_json(category_list, category_object)
    category_object = category2
    category_list = write_json(category_list, category_object)
    pull_json(file_output, category_list)