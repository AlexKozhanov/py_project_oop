from product import Product
from category import Category
from function import read_json, pull_json
import json

file_input = '../config/products.json'
file_output = '../config/output.json'


def main():
    # Чтение данных из json
    category_list = []
    product_list = []
    read_json(file_input, category_list, product_list)

    # Распаковка данных из json
    product1 = product_list[0]
    product2 = product_list[1]
    product3 = product_list[2]

    category1 = category_list[0]
    category2 = category_list[1]

    # Основная программа
    print(category1.products) # До обработки
    category1.print_products_all(category1.products) ## использование метода класса Категория
    product4 = product_list[3]
    category1.add_product(product4)
    print(category1.products) # После обработки
    category1.print_products_all(category1.products) ## использование метода класса Категория
    print(category1.product_count)

    new_product = Product.new_product(
        {"name": "Samsung A55",
         "description": "128GB, Серый цвет, 200MP камера",
         "price": 150000.0,
         "quantity": 1}
    )
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)

    # Запись данных в json
    category_list = []
    category_list.append(Category.decoder(category1))
    category_list.append(Category.decoder(category2))
    pull_json(file_output, category_list)

if __name__ == "__main__":
    main()
