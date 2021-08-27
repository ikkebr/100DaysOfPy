#!/usr/bin/env python3

name = input("What's your name? ")  # prompts the user to enter a name
age = input("What's your age? ")  # prompts the user to enter an age
salary = input("What's your salary? ")  # prompts the user to enter a salary

print(name, type(name))  # name is a str
print(age, type(age))  # age is a str
print(salary, type(salary))  # salary is a str

# If we want to use age and salary as numbers, we need to do the proper type conversions
age = int(age)  # converts age from str to int
salary = float(salary)  # converts salary from str to float
print(age, type(age))  # age is now an int
print(salary, type(salary))  # salary is now a float
