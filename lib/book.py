#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
   
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        try:
            value = int(value)
        except ValueError:
            raise ValueError("Page count must be an integer")
   
   
        if value <= 0:
            raise ValueError("Page count must be an integer")

    def turn_page(self):
        return "Flipping the page... wow, you read fast!"
   