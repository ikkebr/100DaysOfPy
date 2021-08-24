#!/usr/bin/env python3

# The = sign is used to bind an identifier (name) to an object
# There is no need to specify the type of object
# You can create new identifiers pretty much anywhere
variable_name = 5

# When the name is bound to an object, an evaluation of that name yields the object
print(variable_name)  # prints 5

# If the name is not bound, it will raise a NameError exception
# print(not_a_variable) raises a NameError: name 'not_a_variable' is not defined

another_variable = "yes!"
print(another_variable)  # prints yes!

having_fun = True
print(having_fun)  # prints True

another_variable = variable_name = 1.0
print(variable_name, another_variable)  # prints 1.0 1.0

first_value, second_value = 5, 6
print(first_value, second_value)  # prints 5 6

a = 0
b = 1
print(a, b)  # prints 0 1

a, b = b, a  # swapping the values of a and b
print(a, b)  # prints 1 0
