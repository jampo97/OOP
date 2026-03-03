import pytest

from src.category import Category


@pytest.fixture
def products_json() -> list[dict]:
    return [{"name": "1", "quantity": 2}, {"name": "2", "quantity": 4}]


def test_category_2(category_my, category_my_2) -> None:
    """Тест класса из 2 элементов"""

    assert category_my.name == "Категория1"
    assert category_my_2.name == "Категория2"
    assert category_my.description == "Описание1"
    assert category_my_2.description == "Описание2"
    assert category_my.products == "Продукт1 0 руб. Остаток: 2 шт.\n" "Продукт2 10 руб. Остаток: 6 шт.\n"
    assert Category.category_count == 2
    assert Category.product_count == 2


def test_category_repeated_name(category_my_3) -> None:
    assert category_my_3.products == "Продукт2 10 руб. Остаток: 6 шт.\n" "Продукт1 15 руб. Остаток: 12 шт.\n"


def test_category_str(category_my) -> None:
    """Тест на отображение информации о категории"""
    assert str(category_my) == "Категория1, количество продуктов: 8 шт."


def test_category_smart_add_new(category_my, smartphone) -> None:
    """Тест выявление ошибки при добавлении продукта не"""
    category_my.add_product(smartphone)
    assert category_my.products == (
        "Продукт1 0 руб. Остаток: 2 шт.\n"
        "Продукт2 10 руб. Остаток: 6 шт.\n"
        "Название смартфона 999.99 руб. Остаток: 10 шт.\n"
    )


def test_category_smart_add_new_err(category_my) -> None:
    """Тест выявление ошибки при добавлении продукта не входящего в класс продуктов и дочерних"""
    with pytest.raises(TypeError):
        category_my.add_product("Not a product")


def test_category_middle_price(category_my):
    """Тест средняя цена категории"""
    assert category_my.middle_price() == 7.5


def test_category_middle_price_err_text(category_my_2, capsys):
    """Тест ошибка ввода при определении средней цены категории"""
    print(category_my_2.middle_price())
    captured = capsys.readouterr()
    assert "Цена всех продуктов равна 0" in captured.out


def test_category_middle_price_err(category_my_2):
    """Тест ошибка ввода при определении средней цены категории"""
    assert category_my_2.middle_price() == 0
