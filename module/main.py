from product import Product
from category import Category
from function import read_json


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

    # Основная программа
    print(str(product1))
    print(str(product2))
    print(str(product3))

    print(str(category1))
    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)

if __name__ == "__main__":
    main()
