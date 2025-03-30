class Category:
    """Класс Категория"""
    name: str
    description: str
    products: list # список товаров категории

    #Переменные на уровне класса
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаём значения атрибутам экземпляра"""
        self.name = name
        self.description = description
        self.products = products
        self.product_count += len(products)
        Category.category_count += 1

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', product_count={self.product_count}, category_count={self.category_count})"
