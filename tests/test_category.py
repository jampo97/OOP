import pytest

from src.category import Category, sum_products_class, sum_products_json


@pytest.fixture
def products_json() -> list[dict]:
    return [{"name": "1", "quantity": 2}, {"name": "2", "quantity": 4}]


def test_category_2(category_my, category_my_2) -> None:
    """Тест класса из 2 элементов"""

    assert category_my.name == "Категория1"
    assert category_my_2.name == "Категория2"
    assert category_my.description == "Описание1"
    assert category_my_2.description == "Описание2"
    assert category_my.products == ("Продукт1 0 руб. Остаток: 2 шт.\n" "Продукт2 10 руб. Остаток: 6 шт.\n")
    assert Category.category_count == 2
    assert Category.product_count == 2


def test_category_repeated_name(category_my_3) -> None:
    assert category_my_3.products == ("Продукт2 10 руб. Остаток: 6 шт.\n" "Продукт1 15 руб. Остаток: 12 шт.\n")


def test_sum_products_json(products_json) -> None:
    """Тест сложения всех товаров в категории (через словарь)"""
    assert sum_products_json(products_json) == 6


def test_sum_products_json_empty() -> None:
    assert sum_products_json([]) == 0


def test_sum_products_json_err(product_my, product_my_2) -> None:
    with pytest.raises(TypeError):
        sum_products_json(1)
    with pytest.raises(TypeError):
        sum_products_json([product_my, product_my_2])


def test_sum_products_class_empty() -> None:
    assert sum_products_class([]) == 0


def test_sum_products_class_err(product_my, product_my_2) -> None:
    with pytest.raises(TypeError) as exc_info:
        sum_products_class(1)
    assert "'int' object is not iterable" in str(exc_info.value)
    with pytest.raises(AttributeError) as exc_info:
        sum_products_class([{}, {}])
    assert "'dict' object has no attribute 'quantity'" in str(exc_info.value)


def test_category_str(category_my) -> None:
    assert str(category_my) == "Категория1, количество продуктов: 8 шт."
