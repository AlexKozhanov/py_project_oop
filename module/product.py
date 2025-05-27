from abc import ABC, abstractmethod
from MyError import MyError

class BaseProduct:
    @abstractmethod
    def __init__(self):
        name: str # Наименование

class MixinProduct:
    # Product('Продукт1', 'Описание продукта', 1200, 10)
    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаём значения атрибутам экземпляра"""
        super().__init__(name, description, price, quantity)
    def __repr__(self):
        """Отображения информации об объекте в режиме отладки"""
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"

class Product(BaseProduct, MixinProduct):
    """Класс Продукты"""
    # name: str  # Наименование
    description: str # Описание
    price: float # цена
    quantity: int # количество в наличии

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаём значения атрибутам экземпляра"""
        super().__init__()
        self.name = name
        self.description = description
        self.__price = price
        if quantity <= 0:
            raise MyError(1)
        else:
            self.quantity = quantity

    def __repr__(self):
        """Отображения информации об объекте в режиме отладки"""
        # return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"
        return super().__repr__()

    def __str__(self):
        """Метод для строкового отображения объекта"""
        return f"{self.name}, {self.price} руб. Остаток {self.quantity} шт."

    def __add__(self, other):
        """Метод, который вызывается при сложении двух объектов """
        return self.price + other.price

    # def __call__(self, *args, **kwargs):
    #     """Метод, который делает созданный объект вызываемым (callable)"""
    #     print(f'Был вызван объект {self}')

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
    def new_product(cls, product_data):
        name = product_data.get("name")
        description = product_data.get("description")
        price = product_data.get("price")
        quantity = product_data.get("quantity")
        return cls(name, description, price, quantity)

    def decoder(self):
        dict_decoder = dict({"name": self.name,
                             "description": self.description,
                             "price": self.price,
                             "quantity": self.quantity
                             })
        return dict_decoder

class Smartphone(Product):
    """Класс Телефоны"""
    efficiency: int # производительность
    model: str # модель
    memory: int # объем встроенной памяти
    color: str # цвет

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Метод, который вызывается при сложении двух объектов """
        if not isinstance(other, Product):
            raise ValueError('Складывать можно только объекты Product и дочерние от них.')
        self.price += other.price
        self.quantity += other.quantity
        return self

    @classmethod
    def new_product(cls, product_dictionary):
        name = product_dictionary.get("name")
        description = product_dictionary.get("description")
        price = product_dictionary.get("price")
        quantity = product_dictionary.get("quantity")
        efficiency = product_dictionary.get('efficiency')
        model = product_dictionary.get('model')
        memory = product_dictionary.get('memory')
        color = product_dictionary.get('color')
        return cls(name, description, price, quantity, efficiency, model, memory, color)

class LawnGrass(Product):
    """Класс Газон"""
    country: str # страна - производитель
    germination_period: str # срок прорастания
    color: str # цвет

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Метод, который вызывается при сложении двух объектов """
        if not isinstance(other, Product):
            raise ValueError('Складывать можно только объекты Product и дочерние от них.')
        self.price += other.price
        self.quantity += other.quantity
        return self

    @classmethod
    def new_product(cls, product_dictionary):
        name = product_dictionary.get("name")
        description = product_dictionary.get("description")
        price = product_dictionary.get("price")
        quantity = product_dictionary.get("quantity")
        country = product_dictionary.get('efficiency')
        germination_period = product_dictionary.get('model')
        color = product_dictionary.get('color')
        return cls(name, description, price, quantity, country, germination_period, color)