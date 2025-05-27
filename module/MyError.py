class MyError(Exception):
    # Атрибуты класса
    message1 = ""
    message2 = ""
    message3 = ""
    def __init__(self, subrc):
        self.subrc = subrc # Код ошибки
        MyError.message1 = "Товар с нулевым количеством не может быть добавлен"

    def __repr__(self):
        """Отображения информации об объекте в режиме отладки"""
        return f"{self.__class__.__name__}('{self.subrc}')"

    def __str__(self):
        """Метод для строкового отображения объекта"""
        match self.subrc:
            case 1:
                return self.message1

    # try:
    #     raise MyError('Моя ошибка')
    # except MyError as er:
    #     print(er)

    # def converting_class(input=dict, text=str):
    #     """Создаёт объекты классов"""
    #     if text == 'Category':
    #         # Преобразование объектов лист в экземпляры класса Категория
    #         exemplar = Category(input.get('name'), input.get('description'), input.get('products'))
    #         return exemplar
    #     elif text == 'Product':
    #         # Преобразование объектов лист в экземпляры класса Продукты
    #         exemplar = Product(input.get('name'), input.get('description'), input.get('price'), input.get('quantity'))
    #         return exemplar
    #     else:
    #         raise MyError(4,"Такого класса нет")  # Потом текст вынести в отдельное место и брать только код текста с ошибкой

    # try:
    #     category1 = converting_class(category1, 'Category')
    #     product1 = converting_class(product1, 'Product')
    # except MyError as er:
    #     print(er)
    #     quit()