from tests.conftest import product_1
def test_init_product(product_test):
    assert product_test.__repr__() == "Product('Nokia', 'ultra', 1000.0, 1)"
    assert product_test.__str__() == "Nokia, 1000.0 руб. Остаток 1 шт."
    # assert product_test.__call__() == "Был вызван объект Nokia, 1000 руб. Остаток 1 шт."
    assert product_test.name == "Nokia"
    assert product_test.description == "ultra"
    assert product_test.price == 1000.0
    assert product_test.quantity == 1

def test_product_add(product_test, product_test_add):
    assert product_test + product_test_add == 3000.0

def test_init_category(category_test):
    assert category_test.__repr__() == "Category('Phone', 'Phone it's good', product_count=1, category_count=1)"
    assert category_test.__str__() == "Phone, количество продуктов: 1 шт."
    # assert category_test.__call__() == "Был вызван объект Phone, количество продуктов: 1 шт."
    assert category_test.name == "Phone"
    assert category_test.description == "Phone it's good"
    assert category_test.products == [product_1]
    assert category_test.product_count == 1
    assert category_test.category_count == 1
