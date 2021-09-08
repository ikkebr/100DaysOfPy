#!/usr/bin/env python3

# List comprehensions can be used to create a list based on the values of an existing sequence

# We can perform transformations (such as mathematical operations)
squares = [x * x for x in range(10)]
print(squares)

# Or filtering so that the list contains only the elements we are looking for
odd_squares = [x for x in squares if x % 2]
print(odd_squares)

even_squares = [x for x in squares if x % 2 == 0]
print(even_squares)

# We can even do products
cartesian_product = [(x, y) for x in range(5) for y in range(5)]
print(cartesian_product)
