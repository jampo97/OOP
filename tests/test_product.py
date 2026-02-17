import pytest

from src.product import Product


def test_product(product_my) -> None:
    assert product_my.name == "Продукт1"
    assert product_my.description == "Описание1"
    assert product_my.price == 0
    assert product_my.quantity == 2


def test_product_new_price_lower(product_my_2) -> None:
    product_my_2.price = 4
    assert product_my_2.price == 10


def test_product_price(product_my_2, capsys) -> None:
    product_my_2.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_product_err_args() -> None:
    with pytest.raises(TypeError):
        Product("1", "2", 3, 4, 5).name


def test_new_product(dict_product) -> None:
    x = Product.new_product(dict_product)
    assert x.name == "Продукт3"
    assert x.description == "Описание3"
    assert x.price == 99
    assert x.quantity == 88


def test_new_product_err() -> None:
    with pytest.raises(TypeError):
        Product.new_product()


def test_del_product(product_my) -> None:
    product_my.del_product()
    assert product_my.name is None
    assert product_my.description is None
    assert product_my.price == 0
    assert product_my.quantity is None


def test_product_str(product_my) -> None:
    assert str(product_my) == "Продукт1 0 руб. Остаток: 2 шт."


def test_product_add(product_my_2, product_my_3) -> None:
    assert product_my_2 + product_my_3 == 210
