from tests.conftest import test_product #импорт переменной для тестирования

def test_init_product(create_product):
    assert create_product.__repr__() == "Product('Nokia', 'ultra', 1000, 1)"
    assert create_product.name == "Nokia"
    assert create_product.description == "ultra"
    assert create_product.price == 1000
    assert create_product.quantity == 1

def test_init_category(create_category):
    assert create_category.__repr__() == "Category('test', 'test for hell', product_count=1, category_count=1)"
    assert create_category.name == "test"
    assert create_category.description == "test for hell"
    assert create_category.products == [test_product]
    assert create_category.product_count == 1
    assert create_category.category_count == 1
