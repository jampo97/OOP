from typing import Optional


class Category:
    """Класс с описанием категории продуктов"""

    name: str  # название
    description: str  # описание
    products: list[Optional[dict]]  # список товаров категории
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Optional[dict]]):
        """Инициализация элемента класса"""
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        if products:
            Category.product_count += len(products)
        else:
            Category.product_count += 0


def sum_products_json(products: list[Optional[dict]]) -> int:
    """Общее количество товаров в данной категории(для json)"""

    return sum(pr["quantity"] for pr in products)


def sum_products_class(products: list[Optional[dict]]) -> int:
    """Общее количество товаров в данной категории(для Class)"""

    return sum(pr.quantity for pr in products)
