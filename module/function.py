from product import Product
from category import Category
import json


def read_json(file):
    """Функция, читает файл и записывает в списки"""
    with open(file, 'r', encoding="UTF-8") as f:
        data = json.load(f) # тут лежит список со словарями

    #Распаковка и запись Продуктов
    dict_products = data[0] # перезаписали словари из списка
    # Из словаря достаём списки Продуктов
    list_Products = dict_products.get('Products')

    #Распаковка и запись Категорий
    dict_categories = data[1] # перезаписали словари из списка
    # Из словаря достаём списки Категорий
    list_categories_1 = dict_categories.get('Category1')
    list_categories_2 = dict_categories.get('Category2')

    return list_Products, list_categories_1, list_categories_2

def write_json(category_list, category_cls_obj):
    """На вход список и экземпляр класса Категория, на выходе лист с категориями"""
    category_list.append(Category.decoder(category_cls_obj))
    return category_list

def pull_json(file, category_out):
    """Функция, записывает в файл данные"""
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(category_out, f, ensure_ascii=False, indent=2)