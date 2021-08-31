#!/usr/bin/env python3

LIMIT = 5
quantity = int(input("What's the quantity? "))

# if the quantity is greater than the limit, we set the quantity to be the limit
if quantity > LIMIT:
    print(f"The quantity you are trying to order is greater than {LIMIT}")
    quantity = LIMIT

# if the quantity is not greater than the limit but greater than 0 we multiply it by two.
elif quantity > 0:
    print(f"{quantity} looks like a valid quantity. Let's multiply it by 2.")
    quantity *= 2

# every other value must be negative, thus an invalid quantity so we set it to 0 instead.
else:
    print(f"{quantity} is not valid. Setting it to 0.")
    quantity = 0


print(f"The final quantity is {quantity}.")
