from product import Product
from category import Category
import json


def read_json(file, category_list = [], product_list = []):
    """Функция, читает файл и записывает в списки"""
    with open(file, 'r', encoding="UTF-8") as f:
        data = json.load(f) # тут лежит словарь

    # Распаковка и запись Категорий в лист
    category1 = data[0]
    category2 = data[1]

    category_list.append(category1)
    category_list.append(category2)

    # Распаковка и запись Продуктов в лист
    product_list1 = category1.get('products')
    product_list2 = category2.get('products')

    product1 = product_list1[0]
    product2 = product_list1[1]
    product3 = product_list1[2]
    product4 = product_list2[0]

    product_list.append(product1)
    product_list.append(product2)
    product_list.append(product3)
    product_list.append(product4)

    return category_list, product_list

def converting_class(category_list, product_list):
    """Создаёт объекты классов"""
    # Преобразование объектов лист в экземпляры класса Категория
    category_list_cass = []
    product_list_cass = []
    for i in category_list:
        category_obg = Category(i.get('name'), i.get('description'), i.get('products'))
        category_list_cass.append(category_obg)
    # category1_class = Category(category1.get('name'), category1.get('description'), category1.get('products'))
    # category2_class = Category(category2.get('name'), category2.get('description'), category2.get('products'))
    # Преобразование объектов лист в экземпляры класса Продукты
    for j in product_list:
        product_obj = Product(j.get('name'), j.get('description'), j.get('price'), j.get('quantity'))
        product_list_cass.append(product_obj)
    return category_list, product_list

def write_json(category_list, category_cls_obj):
    """На вход список и экземпляр класса Категория, на выходе лист с категориями"""
    category_list.append(Category.decoder(category_cls_obj))
    return category_list

def pull_json(file, category_out):
    """Функция, записывает в файл данные"""
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(category_out, f, ensure_ascii=False, indent=2)