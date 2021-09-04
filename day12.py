#!/usr/bin/env python3

# The while statement can be used to perform repeated execution.
# The loop-body will execute as long as the condition evaluates to True.
# It is not guaranteed that the loop-body will ever be executed.
# Execution will depend on the starting value of count since the condition is count <= 10.
count = 0
while count <= 10:
    print(f"The current count is {count}")
    count += 1


# We can also use lists as the condition for a while
# A non-empty list will evaluate to True
# An empty list will evaluate to False
my_favorite_things = ["Pizza", 42, 3.50]
while my_favorite_things:
    element = my_favorite_things.pop()  # we pop the last element from the list
    print(element, type(element))

print(my_favorite_things)  # the list is now empty
