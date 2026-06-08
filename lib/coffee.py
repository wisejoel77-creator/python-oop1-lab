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
        if value not in ['small', 'medium', 'large']:
            raise ValueError("Size must be 'small', 'medium', or 'large'")
        self._size = value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    def tip(self):
        print("This coffee is great! Here is a tip!")
        self.price += 1

size = input("Enter coffee size (Small, Medium, Large): ")
price = float(input("Enter coffee price: "))

coffee = Coffee(size, price)