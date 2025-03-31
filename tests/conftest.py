import pytest
from module.product import Product
from module.category import Category

test_product = Product("Nokia", "ultra", 1000, 1)
test_category = Category("test", "test for hell", [test_product])

@pytest.fixture
def create_product():
    return test_product

@pytest.fixture
def create_category():
    return test_category