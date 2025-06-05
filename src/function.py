from product import Product
from category import Category
from MyError import MyError
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

def converting_class(input = dict, text = str):
    """Создаёт объекты классов"""
    if text == 'Category':
        # Преобразование объектов лист в экземпляры класса Категория
        exemplar = Category(input.get('name'), input.get('description'), input.get('products'))
        return exemplar
    elif text == 'Product':
        # Преобразование объектов лист в экземпляры класса Продукты
        exemplar = Product(input.get('name'), input.get('description'), input.get('price'), input.get('quantity'))
        return exemplar
    else:
        raise MyError(4, "Такого класса нет") # Потом текст вынести в отдельное место и брать только код текста с ошибкой

def write_json(category_list, category_cls_obj):
    """На вход список и экземпляр класса Категория, на выходе лист с категориями"""
    category_list.append(Category.decoder(category_cls_obj))
    return category_list

def pull_json(file, category_out):
    """Функция, записывает в файл данные"""
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(category_out, f, ensure_ascii=False, indent=2)