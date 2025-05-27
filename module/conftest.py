import pytest
from product import Product, Smartphone, LawnGrass
from category import Category

test_product = Product("Nokia", "ultra", 1000, 1)
test_product_add = Product("Nokia", "ultra", 2000, 1)
test_smartphone = Smartphone("Nokia", "3310", 1000, 1, 100.0, "3300", 128, "синий")
test_lawngrass = LawnGrass("травка", "супер травка", 100, 10, "Куба", "5 дней", "зеленая")
test_category = Category("test", "test for hell", [test_smartphone])

@pytest.fixture
def product_test():
    return test_product

@pytest.fixture
def product_add_test():
    return test_product_add

@pytest.fixture
def category_test():
    return test_category

@pytest.fixture
def smartphone_test():
    return test_smartphone

@pytest.fixture
def lawngrass_test():
    return test_lawngrass