from src.category import Category
from src.product import Product

class ProductIterator:
    def __init__(self, category):
        self.category = category
        self.products = self.category.products.split("\n")
        self.index = -1
    def __iter__(self):

        return self

    def __next__(self):
        if self.index + 1 < len(self.products):
            self.index += 1
            return self.products[self.index]
        else:
            raise StopIteration



if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    iter = ProductIterator(category1)

    for i in iter:
        print(i)  # 1 2 3
    #
    print(iter[1])