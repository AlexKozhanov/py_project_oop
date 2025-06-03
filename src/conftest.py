import pytest
from product import Product, Smartphone, LawnGrass
from category import Category

test_product1 = Product("Nokia", "ultra", 1000.0, 1)
test_product2 = Product("Nokla", "Pultra", 2000.0, 1)
test_smasrtphone = Smartphone("Nokia", "3310", 1000.0, 1, 100.0, "3300", 128, "синий")
test_lawnGrass = LawnGrass("травка", "супер травка", 100, 10, "Куба", "5 дней", "зеленая")
test_category = Category("Phone", "Phone it's good",[test_smasrtphone])

@pytest.fixture
def product_test():
    return test_product1

@pytest.fixture
def product_test_add():
    return test_product2

@pytest.fixture
def category_test():
    return test_category