import pytest
from module.category import Category
from module.product import Product

test_product1 = Product("Nokia", "ultra", 1000.0, 1)
test_product2 = Product("Nokla", "Pultra", 2000.0, 1)
test_category = Category("Phone", "Phone it's good", [test_product1])

@pytest.fixture
def product_test():
    return test_product1

@pytest.fixture
def product_test_add():
    return test_product2

@pytest.fixture
def category_test():
    return test_category