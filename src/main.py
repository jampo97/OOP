import json
import os
from pathlib import Path

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphones import Smartphone


def open_json(project_name: str) -> list[dict]:
    """Открываем json файл"""

    filename = os.path.join(Path(__file__).resolve().parents[1], "data", project_name)
    data = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("Ошибка декодирования")
    except FileNotFoundError:
        print("Файл не найден")
    return data


def json_to_object(category_list: list) -> list:
    """Создаем список элементов классов"""

    cats = []
    for cat in category_list:
        products = []
        for product in cat["products"]:
            products.append(Product(**product))
        cat["products"] = products
        cats.append(Category(**cat))
    return cats


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(category1)
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(category2)
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
    print(Smartphone.__mro__)
    print(LawnGrass.__mro__)
