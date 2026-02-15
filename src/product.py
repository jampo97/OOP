class Product:
    """Класс с описанием продукта"""

    name: str  # название
    description: str  # описание
    price: float  # цена
    quantity: int  # количество в наличии

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация элемента класса"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """ Oтображениe информации об объекте класса для пользователей"""
        return f"{self.name} {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """ Полная стоимость 2 товаров на складе"""
        return (self.__price * self.quantity) + (other.__price * other.quantity)

    @property
    def price(self):
        """Геттер для атрибута «цена»"""

        float_price = self.__price
        return float_price

    @price.setter
    def price(self, new_price: float):
        """Сеттер для атрибута «цена»"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        elif self.__price < new_price:
            user_input = input("Цена уменьшилась. все верно?Y/N")
            if user_input == "Y":
                self.__price
            else:
                self.__price = new_price

    @classmethod
    def new_product(cls, new_prod: dict):
        """Создает новый экземпляр на основе словаря"""

        return cls(new_prod["name"], new_prod["description"], new_prod["price"], new_prod["quantity"])

    def del_product(self):
        """Обнуление значений экземпляра"""
        self.name = None
        self.description = None
        self.__price = 0
        self.quantity = None
