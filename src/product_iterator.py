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
