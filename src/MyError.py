class MyError(Exception):
    def __init__(self, subrc, message):
        self.subrc = subrc # Код ошибки
        self.message = message # Текст ошибки
        # 0 - всё хорошо
        # 4 - ошибка

    def __repr__(self):
        """Отображения информации об объекте в режиме отладки"""
        return f"{self.__class__.__name__}('{self.subrc}', '{self.message}')"

    def __str__(self):
        """Метод для строкового отображения объекта"""
        return f"Ошибка {self.subrc} - {self.message}"

    # try:
    #     raise MyError('Моя ошибка')
    # except MyError as er:
    #     print(er)