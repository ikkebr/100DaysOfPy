#!/usr/bin/env python3

empty_list = list()
another_empty_list = []

# creating a list with two elements using the list function
weekend = list(("Saturday", "Sunday"))
print(f"The first day of the weekend is {weekend[0]}")  # Saturday

# creating a list with five elements using the [] constructor
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(f"The first day of the week is {days_of_the_week[0]}")  # Monday

# adding both lists together
week = days_of_the_week + weekend
print(f"The last day of the week is {week[-1]}")  # Sunday

# We can append elements to a list using append
week.append("An extra day")
print(week)

# We can remove elements from a list using pop
week.pop()  # no more Extra days!
print(week)

week.pop(0)  # no more Mondays!
print(week)

# lists can also hold values of different types
my_favorite_things = [42, "Computers"]
print(my_favorite_things)

# we can even have lists of lists
my_favorite_things.append(weekend)
print(my_favorite_things)
