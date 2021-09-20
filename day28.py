#!/usr/bin/env python3

# the doctest module allows us to write "executable documentation"
# we can model test cases as examples inside the doctstrings
# and doctest will execute these examples
# comparing the actual output with the expected output
def calculate_distance(x, y):
    """Calculates the distance of two points in the real line.

    >>> calculate_distance(0,1)
    1.0
    >>> calculate_distance(0, -1)
    1.0
    >>> calculate_distance(1, -1)
    2.0
    >>> calculate_distance(1, -10)
    11.0

    # This test example will fail as the function returns a float
    >>> calculate_distance(5, 5)
    0
    """
    return ((x - y) ** 2) ** 0.5


if __name__ == "__main__":
    import doctest

    doctest.testmod()
