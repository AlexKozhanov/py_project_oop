from MyError import MyError
from function import read_json, pull_json, write_json, converting_class

file_input = '../config/products.json'
file_output = '../config/output.json'

def main():
    # Чтение данных из json
    category_list = []
    product_list = []
    read_json(file_input, category_list, product_list)

    # Распаковка данных из json
    category1 = category_list[0]
    product1 = product_list[0]
    product2 = product_list[1]
    product3 = product_list[2]
    # Обработка данных в экземпляры класса
    try:
        category1 = converting_class(category1, 'Category')
        product1 = converting_class(product1, 'Product')
        product2 = converting_class(product2, 'Product')
        product3 = converting_class(product3, 'Product')
    except MyError as er:
        print(er)
        quit()

    # Основная программа
    print(str(product1))
    print(str(product2))
    print(str(product3))

    print(str(category1))
    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)


    # Запись данных в json
    category_list = []
    category_list = write_json(category_list, category1)
    pull_json(file_output, category_list)

if __name__ == "__main__":
    main()
