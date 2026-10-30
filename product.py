import re

class Product:
    _total_count = 0

    def __init__(self, name, sku, price, quantity):
        if not self.is_valid_sku(sku):
            raise ValueError(f"Invalid SKU: {sku}")
        self.name = name
        self.sku = sku
        self.price = price
        self.quantity = quantity
        Product._total_count += 1

    def __repr__(self):
        return f"Product({self.name!r}, {self.sku!r}, {self.price}, {self.quantity})"

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number")
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = float(value)

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("Quantity must be an integer")
        if value < 0:
            raise ValueError("Quantity cannot be negative")
        self._quantity = value

    @property
    def line_value(self):
        return self.price * self.quantity

    @property
    def is_low_stock(self):
        return self.quantity < 5

    @classmethod
    def from_csv_line(cls, line):
        parts = [p.strip() for p in line.split(",")]
        return cls(parts[0], parts[1], float(parts[2]), int(parts[3]))

    @staticmethod
    def is_valid_sku(sku):
        return bool(re.fullmatch(r"[A-Za-z]{3}\d{3}", sku))

    @classmethod
    def count(cls):
        return cls._total_count
