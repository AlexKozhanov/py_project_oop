from tests.conftest import test_smartphone #импорт переменной для тестирования

def test_init_product(product_test):
    assert product_test.__repr__() == "Product('Nokia', 'ultra', 1000, 1)"
    assert product_test.__str__() == "Nokia, 1000 руб. Остаток 1 шт."
    assert product_test.name == "Nokia"
    assert product_test.description == "ultra"
    assert product_test.price == 1000
    assert product_test.quantity == 1

def test_product_add(product_test, product_add_test):
    assert product_test + product_add_test == 3000.0

def test_init_category(category_test):
    assert category_test.__repr__() == "Category('test', 'test for hell', product_count=1, category_count=1)"
    assert category_test.__str__() == "test, количество продуктов: 1 шт."
    assert category_test.name == "test"
    assert category_test.description == "test for hell"
    assert category_test.products == [test_smartphone]
    assert category_test.product_count == 1
    assert category_test.category_count == 1

def test_init_Smartphone(smartphone_test):
    assert smartphone_test.__repr__() == "Smartphone('Nokia', '3310', 1000, 1)"
    assert smartphone_test.__str__() == "Nokia, 1000 руб. Остаток 1 шт."
    assert smartphone_test.name == 'Nokia'
    assert smartphone_test.description == '3310'
    assert smartphone_test.price == 1000
    assert smartphone_test.quantity == 1
    assert smartphone_test.efficiency == 100.0
    assert smartphone_test.model == '3300'
    assert smartphone_test.memory == 128
    assert smartphone_test.color == 'синий'

def test_init_lawn_grass(lawngrass_test):
    assert lawngrass_test.__repr__() == "LawnGrass('Grass', 'Super Grass', 100, 10)"
    assert lawngrass_test.__str__() == "Grass, 100 руб. Остаток 10 шт."
    assert lawngrass_test.name == 'Grass'
    assert lawngrass_test.description == 'Super Grass'
    assert lawngrass_test.price == 100
    assert lawngrass_test.quantity == 10
    assert lawngrass_test.country == 'Cuba'
    assert lawngrass_test.germination_period == '5 day'
    assert lawngrass_test.color == 'green'
