import json
import os
from pathlib import Path

from src.category import Category
from src.product import Product


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


# if __name__ == "__main__":
#     my_data = open_json("products.json")
#     res = json_to_object(my_data)
#     # sum_0 = sum_products_class(res[0].products)
#     print(res[0].name)
#     print(res[0].description)
#     print(res[0].products)
#     print(len(res[0].products))
#     print(res[0].category_count)
#     print(res[0].product_count)
#     # print(sum_0)

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
