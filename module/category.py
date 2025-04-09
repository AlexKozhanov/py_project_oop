from product import Product
import json
class Category:
    """Класс Категория"""
    name: str
    description: str
    products: Product # список товаров категории

    #Переменные на уровне класса
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаём значения атрибутам экземпляра"""
        self.name = name
        self.description = description
        self.__products = products # Приватный атрибут
        self.product_count += len(products)
        Category.category_count += 1

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', product_count={self.product_count}, category_count={self.category_count})"

    def __dict__(self):
        return {
                "name": self.name,
                "description": self.description
               }

    @property
    def products(self):
        return self.__products

    @property
    def print_products(self):
        return f"{self.__products}, Остаток: {self.product_count}"

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)

    def add_product(self, new_product = Product):
        self.products.append(new_product) # использование сеттера?
        self.product_count += 1