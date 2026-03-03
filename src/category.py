from typing import Optional

from src.product import Product


class Category:
    """Класс с описанием категории продуктов"""

    name: str  # название
    description: str  # описание
    products: list[Optional[dict]]  # список товаров категории
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """Инициализация элемента класса"""

        self.name = name
        self.description = description

        # Поиск повторяющихся значений по названиям продуктов и изменение их значений
        all_names = [product.name for product in products]
        duplicates = []  # повторки
        seen = []  # уникальные названия
        for name in all_names:  # Раскидываем все названия на 2 списка - уникальные и повторки
            if name not in seen:
                seen.append(name)
            elif name in seen:
                duplicates.append(name)
        for repeated_name in duplicates:  # Работаем с каждой повторкой в отдельности
            first_time = True
            for product in products:
                if product.name == repeated_name:  # Если название в списке продуктов совпало с повторкой
                    if first_time:  # Записываем значения если это впервые
                        first_price = product.price
                        first_quantity = product.quantity
                        first_time = False
                        product.del_product()  # Больше этот продукт не нужен и все его значения = None
                    else:  # В каждый последующий дупликат
                        now_price = product.price
                        product.price = max(now_price, first_price)
                        product.quantity += first_quantity
                        break
        products = [product for product in products if product.name is not None]  # небольшой костыль

        self.__products = products if products else []
        Category.category_count += 1
        if products:
            Category.product_count += len(products)
        else:
            Category.product_count += 0

    def __str__(self):
        all_products = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {all_products} шт."

    @property
    def products(self):
        """Геттер для приватного атрибута products"""

        new_string = ""
        for product in self.__products:
            new_string += f"{str(product)}\n"
        return new_string

    def add_product(self, product):
        """Добавление продукта в атрибут products"""

        if isinstance(product, Product):
            Category.product_count += 1 if product else print("error")
            self.__products.append(product)
        else:
            raise TypeError

    def middle_price(self):
        """Подсчет средней цены товаров в категории"""

        all_products = sum(product.quantity for product in self.__products)
        all_price = sum(product.price * product.quantity for product in self.__products)
        try:
            res = all_price / all_products
        except ZeroDivisionError:
            print("Цена всех продуктов равна 0")
            return 0
        else:
            return res
