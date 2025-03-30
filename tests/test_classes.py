import pytest
from module.product import Product
from module.category import Category

product_test = Product("Nokia", "ultra", 1000, 1)
category_test = Category("test", "test for hell", [product_test])

def test_init_product():
    assert product_test.__repr__() == "Product('Nokia', 'ultra', 1000, 1)"

def test_init_category():
    assert category_test.__repr__() == "Category('test', 'test for hell', product_count=1, category_count=1)"
    assert category_test.name == 'test'
    assert category_test.product_count == 1
    assert category_test.category_count == 1
