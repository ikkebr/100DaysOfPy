#!/usr/bin/env python3

units = 7  # 7 is an int
price = 129.66  # 129.66 is a float

# If types are compatible, Python performs an implicit type conversion
total = units * price  # the result is also a float
print(total)  # prints 907.62

tax_string = "129"  # "129" is a str
#new_total = total + tax_string  # This will raise a TypeError
# We can't add a string to a number! What would be the result? Python will not guess.

new_total = total + float(tax_string)  # we needed to use an explicit type conversion
print(new_total)  # prints 1036.62

# Even though we cannot add a str to int without converting, we can multiply a str by an int!
delimiter = "*#"
how_many = 5
print(delimiter * how_many)  # prints *#*#*#*#*#
