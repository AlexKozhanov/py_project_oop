class Product:
    """Класс Продукты"""
    name: str
    description: str
    price: float
    quantity: int # количество в наличии

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаём значения атрибутам экземпляра"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"
