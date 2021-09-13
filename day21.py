#!/usr/bin/env python3

# We can also have functions that yield more than one value
# Remember the numbers that were multiples of 3, 5, 7 and 13?
# What if we could generate them all!?!
def generate_multiples(how_many=-1):
    number = 0
    while True and how_many:
        if number % 3 == 0 and number % 5 == 0 and number % 7 == 0 and number % 13 == 0:
            how_many -= 1
            yield number
        number += 1

# Let's generate the first 10 multiples
for n in generate_multiples(how_many = 10):
    print(n)

# We can also get these multiples one by one, manually
multiples = generate_multiples(4) # we instantiate the generator
print(next(multiples)) # we get the first number
print(next(multiples)) # we get the second number
print(next(multiples)) # we get the third number
print(next(multiples)) # we get the fourth

# Let's generate an infinite amount of multiples
for n in generate_multiples():
    print(n) # this will print a multiple and wait for the next one
    # this will not stop. Press ctrl+c or ctrl+z to quit.
    
