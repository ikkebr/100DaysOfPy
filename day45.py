#!/usr/bin/env python3

# We can define our own iterators following the __iter__ protocol.
# We must define an __iter__ and a __next__ method.
class Paginator(object):
    def __init__(self, page_size=5, total_pages=20):
        self.page_size = page_size
        self.total_pages = total_pages

    # The __iter__ method returns the iterator itself
    def __iter__(self):
        self.current_item = 0
        return self

    # The __next__ method returns the next item in the sequence
    def __next__(self):
        current = self.current_item
        if current > self.total_pages:
            raise StopIteration
        self.current_item += self.page_size
        return [current, self.current_item]


for page in Paginator(page_size=3, total_pages=20):
    print(page)
