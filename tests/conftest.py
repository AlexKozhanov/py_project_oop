import pytest
from module.product import Product, Smartphone, LawnGrass
from module.category import Category

test_product = Product("Nokia", "ultra", 1000, 1)
test_smasrtphone = Smartphone("Nokia", "3310", 1000, 1, 100.0, "3300", 128, "синий")
test_lawnGrass = LawnGrass("трака", "супер травка", 100, 10, "Куба", "5 дней", "зеленая")
test_category = Category("test", "test for hell", [test_smasrtphone])

@pytest.fixture
def create_product():
    return test_product

@pytest.fixture
def create_category():
    return test_category