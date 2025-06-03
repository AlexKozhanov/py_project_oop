#INCLUDE:
from myerror import MyError
from function import read_json, pull_json, write_json
from category import Category
from product import Product, Smartphone, LawnGrass
import json

#DATA:
file_input = '../config/products.json'
file_output = '../config/output.json'

#INITIALIZATION.
def main(category_smartphones, category_grass, smartphone1, smartphone2, smartphone3, grass1, grass2):
    """Основная программа"""
    # smartphone
    print(smartphone1.name)
    print(smartphone1.description)
    print(smartphone1.price)
    print(smartphone1.quantity)
    print(smartphone1.efficiency)
    print(smartphone1.model)
    print(smartphone1.memory)
    print(smartphone1.color)

    print(smartphone2.name)
    print(smartphone2.description)
    print(smartphone2.price)
    print(smartphone2.quantity)
    print(smartphone2.efficiency)
    print(smartphone2.model)
    print(smartphone2.memory)
    print(smartphone2.color)

    print(smartphone3.name)
    print(smartphone3.description)
    print(smartphone3.price)
    print(smartphone3.quantity)
    print(smartphone3.efficiency)
    print(smartphone3.model)
    print(smartphone3.memory)
    print(smartphone3.color)

    # grass
    print(grass1.name)
    print(grass1.description)
    print(grass1.price)
    print(grass1.quantity)
    print(grass1.country)
    print(grass1.germination_period)
    print(grass1.color)

    print(grass2.name)
    print(grass2.description)
    print(grass2.price)
    print(grass2.quantity)
    print(grass2.country)
    print(grass2.germination_period)
    print(grass2.color)

    smartphone_sum = smartphone1 + smartphone2
    print(smartphone_sum)

    grass_sum = grass1 + grass2
    print(grass_sum)

    try:
        invalid_sum = smartphone1 + grass1
    except MyError:
        print("Возникла ошибка MyError при попытке сложения")
    else:
        print("Не возникла ошибка MyError при попытке сложения")

    # category
    category_smartphones.add_product(smartphone3)

    print(category_smartphones.products)

    print(Category.product_count)

    try:
        category_smartphones.add_product("Not a product")
    except MyError as er:
        print("Возникла ошибка MyError при добавлении не продукта")
        print(er)
    else:
        print("Не возникла ошибка MyError при добавлении не продукта")

if __name__ == "__main__":
    # Чтение данных из json
    list_Smartphone_products, list_LawnGrass_products, \
    list_Smartphone_categories, list_LawnGrass_categories = read_json(file_input) # тут словари в списках

    # Распаковка данных из json
    category_smartphones = list_Smartphone_categories[0] # тут уже словари
    category_grass = list_LawnGrass_categories[0]
    smartphone1 = list_Smartphone_products[0]
    smartphone2 = list_Smartphone_products[1]
    smartphone3 = list_Smartphone_products[2]
    grass1 = list_LawnGrass_products[0]
    grass2 = list_LawnGrass_products[1]

    # Обработка данных в экземпляры класса
    category_smartphones = Category.new_category(category_smartphones, list_Smartphone_products)
    category_grass = Category.new_category(category_grass, list_LawnGrass_products)
    smartphone1 = Smartphone.new_product(smartphone1)
    smartphone2 = Smartphone.new_product(smartphone2)
    smartphone3 = Smartphone.new_product(smartphone3)
    grass1 = LawnGrass.new_product(grass1)
    grass2 = LawnGrass.new_product(grass2)

    # Основная программа
    main(category_smartphones, category_grass, smartphone1, smartphone2, smartphone3, grass1, grass2)

    # Кодировка данных в json
    category_smartphones.products[3] = Product.decoder(category_smartphones.products[3])  # для кодировки в json
    category_list = []
    category_list = write_json(category_list, category_smartphones)
    pull_json(file_output, category_list)