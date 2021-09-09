#!/usr/bin/env python3

# Dictionary comprehensions are also a thing!
# We can use a dict comprehension to create a dictionary from an existing sequence
people = [("Henrique", 33), ("Paulo", 20), ("Rafael", 11), ("Carlos", 10)]
people_dict = {name: age for name, age in people}
print(people_dict)

# We can also do filtering using if conditions
underage_people = {name: age for name, age in people if age < 18}
print(underage_people)

# Or transformations
underage_transformation = {name: age + 10 for name, age in underage_people.items()}
print(underage_transformation)

# Or everything together
squares_of_odd_numbers = {
    number: number * number for number in range(10) if number % 2 != 0
}
print(squares_of_odd_numbers)