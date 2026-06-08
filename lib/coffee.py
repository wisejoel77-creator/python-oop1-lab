#!/usr/bin/env python3
class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        value = str(value).strip().lower()

        if value not in ['small', 'medium', 'large']:
            raise ValueError("Size must be 'small', 'medium', or 'large'")

        self._size = value.title()  

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = float(value)

        if self._price < 0:
            raise ValueError("Price cannot be negative")

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self._price += 1






























