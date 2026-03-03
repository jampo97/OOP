import pytest

from src.product import Product


def test_product(product_my) -> None:
    assert product_my.name == "Продукт1"
    assert product_my.description == "Описание1"
    assert product_my.price == 0
    assert product_my.quantity == 2


def test_product_err() -> None:
    """Тест действие при понижении цены до нуля и ниже"""
    with pytest.raises(ValueError):
        Product("Продукт", "Описание", 3, 0)


def test_smartphone(smartphone) -> None:
    assert smartphone.name == "Название смартфона"
    assert smartphone.description == "Описание"
    assert smartphone.price == 999.99
    assert smartphone.quantity == 10
    assert smartphone.efficiency == 99.9
    assert smartphone.model == "Модель смартфона"
    assert smartphone.memory == 64
    assert smartphone.color == "White"


def test_lawn_grass(lawn_grass) -> None:
    assert lawn_grass.name == "Название травы"
    assert lawn_grass.description == "Описание"
    assert lawn_grass.price == 999.99
    assert lawn_grass.quantity == 10
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "Лето"
    assert lawn_grass.color == "Зеленый цвет"


def test_product_new_price_lower(product_my_2) -> None:
    """Тест действие при понижении цены - возврат старой"""
    product_my_2.price = 4
    assert product_my_2.price == 10


def test_product_price(product_my_2, capsys) -> None:
    """Тест действие при понижении цены до нуля и ниже"""
    product_my_2.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_product_err_args() -> None:
    """Тест действие при вводе неверного количества аргументов"""
    with pytest.raises(TypeError):
        Product("1", "2", 3, 4, 5).name


def test_new_product(dict_product) -> None:
    """Тест новый продукт"""
    x = Product.new_product(dict_product)
    assert x.name == "Продукт3"
    assert x.description == "Описание3"
    assert x.price == 99
    assert x.quantity == 88


def test_new_product_err() -> None:
    """Тест ошибка при вводе нового продукта"""
    with pytest.raises(TypeError):
        Product.new_product()


def test_del_product(product_my) -> None:
    product_my.del_product()
    assert product_my.name is None
    assert product_my.description is None
    assert product_my.price == 0
    assert product_my.quantity is None


def test_product_str(product_my) -> None:
    """Тест на отображение информации о продукте"""
    assert str(product_my) == "Продукт1 0 руб. Остаток: 2 шт."


def test_product_add(product_my_2, product_my_3) -> None:
    """Тест на сложение продуктов из 1 класса"""
    assert product_my_2 + product_my_3 == 210


def test_product_add_err(product_my, smartphone) -> None:
    """Тест на ошибку сложения разных классов"""
    with pytest.raises(TypeError):
        result = product_my + smartphone
        assert result
