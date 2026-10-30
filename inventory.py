from product import Product

class Inventory:
    def __init__(self):
        self.products = {}

    def add(self, product):
        self.products[product.sku] = product

    def remove(self, sku):
        return self.products.pop(sku, None)

    def find(self, sku):
        return self.products.get(sku)

    def total_value(self):
        return sum(p.line_value for p in self.products.values())

    @classmethod
    def from_lines(cls, lines):
        inv = cls()
        for line in lines:
            inv.add(Product.from_csv_line(line))
        return inv
