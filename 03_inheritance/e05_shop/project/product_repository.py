from typing import List
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        return next(filter(lambda x: x.name == product_name, self.products))

    def remove(self, product_name: str):
        try:
            self.products.remove(next(filter(lambda x: x.name == product_name, self.products)))
        except StopIteration:
            return None

    def __repr__(self):
        product_list = [f'{x.name}: {x.quantity}' for x in self.products]
        return '\n'.join(product_list)
