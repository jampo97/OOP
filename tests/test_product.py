import pytest

from src.product import Product


def test_product(product_my) -> None:
    assert product_my.name == "Название продукта"
    assert product_my.description == "Описание продукта"
    assert product_my.price == 99.99
    assert product_my.quantity == 5


def test_product_err_args() -> None:
    with pytest.raises(TypeError):
        Product("1", "2", 3, 4, 5).name
