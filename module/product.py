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
        self.__price = price
        self.quantity = quantity

    def __repr__(self):
        """Отображения информации об объекте в режиме отладки"""
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"

    def __str__(self):
        """Метод для строкового отображения объекта"""
        return f"{self.name}, {self.price} руб. Остаток {self.quantity} шт."

    def __add__(self, other):
        """Метод, который вызывается при сложении двух объектов """
        self.name += other.name
        self.description += other.description
        self.price += other.price
        self.quantity += self.quantity

    def __call__(self, *args, **kwargs):
        """Метод, который делает созданный объект вызываемым (callable)"""
        print(f'Был вызван объект {self}')

    @property
    def price(self):
        return self.__price # геттер

    @price.setter
    def price(self, price):
         if price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
         else:
            self.__price = price

    @property
    def str_product(self):
        return f"{self.name}, {self.price} руб. Остаток {self.quantity} шт."

    @classmethod
    def new_product(cls, product_dictionary):
        name = product_dictionary['name']
        description = product_dictionary['description']
        price = product_dictionary['price']
        quantity = product_dictionary['quantity']
        return cls(name, description, price, quantity)
