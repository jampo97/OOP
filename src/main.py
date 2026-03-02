import json
import os
from pathlib import Path

from src.category import Category
# from src.lawn_grass import LawnGrass
from src.product import Product

# from src.smartphones import Smartphone


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
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError:
        print(
            "Возникла ошибка ValueError "
            "прерывающая работу программы при попытке добавить продукт с нулевым количеством"
        )
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
