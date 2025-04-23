from product import Product

class Category:
    """Класс Категория"""
    name: str
    description: str
    products: Product # список товаров категории

    # Переменные на уровне класса/Атрибуты класса Category
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

    def __str__(self):
        """Метод для строкового отображения объекта"""
        return f"-----/№{self.category_count}, Категория - {self.name}/-----\n" \
               f"Кол-во {self.name} =  {self.product_count}\n" \
               f"Описание: {self.description}"

    def __len__(self):
        """ Метод, который вызывается при применении функции len"""
        return len(f'{self.name}{self.description}')

    def __add__(self, other):
        """Метод, который вызывается при сложении двух объектов"""
        self.name += other.name
        self.description += other.description
        self.product_count += other.product_count

    def __call__(self, *args, **kwargs):
        """Метод, который делает созданный объект вызываемым (callable) """
        print(f'Был вызван объект {self}')

    @property
    def products(self):
        return self.__products

    @classmethod
    def print_products_all(cls, products_of_category):
        """Название продукта, 80 руб. Остаток: 15 шт."""
        for i in products_of_category:
            one_products_of_category = Product(i.get('name'), i.get('description'), i.get('price'), i.get('quantity'))
            print(str(one_products_of_category))

    def add_product(self, new_product):
        """Добавляет в список товаров категории товар вида Список"""
        self.products.append(new_product)
        self.product_count += 1

    def decoder(self):
        dict_decoder = dict({"name": self.name,
                             "description": self.description,
                             "product_count": self.product_count,
                             "products": self.products
                             })
        return dict_decoder

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield (attr, value)
