# encoding: utf-8
import pytest

from src.category import Category
from src.product import Product

product_1 = Product("Nokia", "ultra", 1000.0, 1)

@pytest.fixture
def product_test():
    return Product("Nokia", "ultra", 1000.0, 1)

@pytest.fixture
def product_test_add():
    return Product("Nokla", "Pultra", 2000.0, 1)

@pytest.fixture
def category_test():
    return Category("Phone", "Phone it's good", [product_1])