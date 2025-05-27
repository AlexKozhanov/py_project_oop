#INCLUDE:
from MyError import MyError
from function import read_json, pull_json, write_json
from category import Category
from product import Product, Smartphone, LawnGrass
import json

#DATA:
file_input = '../config/products.json'
file_output = '../config/output.json'

#INITIALIZATION.
def main(category1, category2, product1, product2, product3):
    """Основная программа"""
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as er:
        print("Возникла ошибка ValueError прерывающая работу "
              "программы при попытке добавить продукт с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")
    print(category1)
    print(category1.middle_price())
    print(category2)
    print(category2.middle_price())

if __name__ == "__main__":
    # Чтение данных из json
    list_Products, list_categories_1, list_categories_2 = read_json(file_input) # тут словари в списках

    # Распаковка данных из json
    category_1 = list_categories_1[0] # тут уже словари
    category_2 = list_categories_2[0]
    product_1 = list_Products[0]
    product_2 = list_Products[1]
    product_3 = list_Products[2]
    list_products_1 = [product_1, product_2, product_3]
    list_products_2 = []

    # Обработка данных в экземпляры класса
    product1 = Product.new_product(product_1)
    product2 = Product.new_product(product_2)
    product3 = Product.new_product(product_3)
    list_products_1 = []
    list_products_1.append(product1)
    list_products_1.append(product2)
    list_products_1.append(product3)
    category1 = Category.new_category(category_1, list_products_1)
    category2 = Category.new_category(category_2, list_products_2)

    # Основная программа
    main(category1, category2, product1, product2, product3)

    # Кодировка данных в json
    # category_smartphones.products[3] = Product.decoder(category_smartphones.products[3])  # для кодировки в json
    # category_list = []
    # category_object = category1
    # category_list = write_json(category_list, category_object)
    # category_object = category2
    # category_list = write_json(category_list, category_object)
    # pull_json(file_output, category_list)