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
    list_Smartphone_products = dict_products.get('Smartphone')
    list_LawnGrass_products = dict_products.get('LawnGrass')

    #Распаковка и запись Категорий
    dict_categories = data[1] # перезаписали словари из списка
    # Из словаря достаём списки Категорий
    list_Smartphone_categories = dict_categories.get('Smartphone')
    list_LawnGrass_categories = dict_categories.get('LawnGrass')

    return list_Smartphone_products, list_LawnGrass_products, list_Smartphone_categories, list_LawnGrass_categories

def write_json(category_list, category_cls_obj):
    """На вход список и экземпляр класса Категория, на выходе лист с категориями"""
    category_list.append(Category.decoder(category_cls_obj))
    return category_list

def pull_json(file, category_out):
    """Функция, записывает в файл данные"""
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(category_out, f, ensure_ascii=False, indent=2)