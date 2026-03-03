import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphones import Smartphone


@pytest.fixture
def product_my():
    return Product("Продукт1", "Описание1", 0, 2)


@pytest.fixture
def product_my_2():
    return Product("Продукт2", "Описание2", 10, 6)


@pytest.fixture
def product_my_3():
    return Product("Продукт1", "Описание1", 15, 10)


@pytest.fixture
def product_my_4():
    return Product("Продукт4", "Описание4", 3, 0)


@pytest.fixture
def category_my(product_my, product_my_2):
    return Category("Категория1", "Описание1", [product_my, product_my_2])


@pytest.fixture
def category_my_2():
    return Category("Категория2", "Описание2", [])


@pytest.fixture
def category_my_3(product_my, product_my_2, product_my_3):
    return Category("Название категории", "Описание категории", [product_my, product_my_2, product_my_3])


@pytest.fixture
def category_my_4(product_my_3, product_my_2, product_my):
    return Category("Название категории", "Описание категории", [product_my_3, product_my_2, product_my])


@pytest.fixture
def all_categories():
    return [
        {
            "name": "phones",
            "description": "android",
            "products": [
                {"name": 11, "description": 12, "price": 13, "quantity": 14},
                {"name": 21, "description": 22, "price": 23, "quantity": 24},
            ],
        },
        {
            "name": "TV",
            "description": "android",
            "products": [{"name": 31, "description": 32, "price": 33, "quantity": 34}],
        },
    ]


@pytest.fixture
def dict_product():
    return {"name": "Продукт3", "description": "Описание3", "price": 99, "quantity": 88}


@pytest.fixture
def product_iterator(category_my_3):
    return ProductIterator(category_my_3)


@pytest.fixture
def product_iterator_none(category_my_2):
    return ProductIterator(category_my_2)


@pytest.fixture
def smartphone():
    return Smartphone("Название смартфона", "Описание", 999.99, 10, 99.9, "Модель смартфона", 64, "White")


@pytest.fixture
def lawn_grass():
    return LawnGrass("Название травы", "Описание", 999.99, 10, "Россия", "Лето", "Зеленый цвет")
