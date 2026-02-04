import pytest

from src.category import Category, sum_products_class, sum_products_json


@pytest.fixture
def products_json() -> list[dict]:
    return [{"name": "1", "quantity": 2}, {"name": "2", "quantity": 4}]


def test_category_2(category_my, category_my_2) -> None:
    """Тест класса из 2 элементов"""

    assert category_my.name == "Название категории"
    assert category_my_2.name == "Название категории2"
    assert category_my.description == "Описание категории"
    assert category_my_2.description == "Описание категории2"
    assert len(category_my.products) == 2
    assert len(category_my_2.products) == 0
    assert Category.category_count == 2
    assert Category.product_count == 2


def test_category_3(category_my) -> None:
    """Добавил еще один элемент в класс"""

    assert Category.category_count == 3
    assert Category.product_count == 4


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


def test_sum_products_class(product_my, product_my_2) -> None:
    """Тест сложения всех товаров в категории (через класс)"""
    assert sum_products_class([product_my, product_my_2]) == 9


def test_sum_products_class_empty() -> None:
    assert sum_products_class([]) == 0


def test_sum_products_class_err(product_my, product_my_2) -> None:
    with pytest.raises(TypeError) as exc_info:
        sum_products_class(1)
    assert "'int' object is not iterable" in str(exc_info.value)
    with pytest.raises(AttributeError) as exc_info:
        sum_products_class([{}, {}])
    assert "'dict' object has no attribute 'quantity'" in str(exc_info.value)
