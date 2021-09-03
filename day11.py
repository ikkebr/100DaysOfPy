#!/usr/bin/env python3

# Creating an empty set
my_set = set()

# Adding element to a set
my_set.add(1)
my_set.add(200)
my_set.add("Henrique")
print(my_set)

# Sets will only store one copy of an object
my_set.add(1)
print(my_set)

# Sets can be used to store distinct values
names = ["Henrique", "Paulo", "Pedro", "Paulo", "Paulo", "Carlos"]
distinct = set(names)
print(distinct)

# Sets can perform set operations (union, intersection, difference)
print(distinct.intersection(my_set))  # only "Henrique" appears in both seths
print(distinct.union(my_set))  # all elements from both sets
print(distinct.difference(my_set))  # only elements from distinct that are not in my_set
print(my_set.difference(distinct))  # only elements from my_set that are not in distinct
