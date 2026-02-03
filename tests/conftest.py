import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_my():
    return Product("Название продукта", "Описание продукта", 99.99, 5)


@pytest.fixture
def product_my_2():
    return Product(1, 2, 3, 4)


@pytest.fixture
def category_my(product_my, product_my_2):
    return Category("Название категории", "Описание категории", [product_my, product_my_2])


@pytest.fixture
def category_my_2():
    return Category("Название категории2", "Описание категории2", None)


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
