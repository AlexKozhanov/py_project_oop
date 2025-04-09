from product import Product
from category import Category
import json


def read_json(file, category_list = [], product_list = []):
    """Функция, которая будет читать файл и создавать объекты классов"""
    with open(file, 'r', encoding="UTF-8") as f:
        data = json.load(f) # тут лежит словарь

    # Распаковка и запись Категорий в лист
    category1 = data[0]
    category2 = data[1]

    category1_class = Category(category1.get('name'), category1.get('description'), category1.get('products'))
    category2_class = Category(category2.get('name'), category2.get('description'), category2.get('products'))

    category_list.append(category1_class)
    category_list.append(category2_class)

    # Распаковка и запись Продуктов в лист
    product_list1 = category1.get('products')
    product_list2 = category2.get('products')

    product1 = product_list1[0]
    product2 = product_list1[1]
    product3 = product_list1[2]
    product4 = product_list2[0]

    product1_class = Product(product1.get('name'),
                             product1.get('description'),
                             product1.get('price'),
                             product1.get('quantity'))
    product2_class = Product(product2.get('name'),
                             product2.get('description'),
                             product2.get('price'),
                             product2.get('quantity'))
    product3_class = Product(product3.get('name'),
                             product3.get('description'),
                             product3.get('price'),
                             product3.get('quantity'))
    product4_class = Product(product4.get('name'),
                             product4.get('description'),
                             product4.get('price'),
                             product4.get('quantity'))

    product_list.append(product1_class)
    product_list.append(product2_class)
    product_list.append(product3_class)
    product_list.append(product4_class)

    return category_list, product_list


def pull_json(file, category_out = Category):
    with open(file, 'w') as f:
        json.dump(category_out.toJSON, f)