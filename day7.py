#!/usr/bin/env python3

LIMIT = 5
quantity = int(input("What's the quantity? "))

# if the quantity is greater than the limit, we set the quantity to be the limit
if quantity > LIMIT:
    print(f"The quantity you are trying to order is greater than {LIMIT}")
    quantity = LIMIT

# if the quantity is not greater than the limit, then we multiply it by two
else:
    print(f"{quantity} looks like a valid quantity. Let's multiply it by 2.")
    quantity *= 2


print(f"The final quantity is {quantity}.")
