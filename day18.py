#!/usr/bin/env python3

# Python can handle imaginary numbers or complex numbers natively!
# We can use j to represent the squareroot of -1

# Calculating the square root of -25 is as easy as calculating the sqrt of 25
# and multiplying it by 1j
sqrt_neg25 = 25 ** 0.5 * 1j
print(sqrt_neg25, sqrt_neg25.real, sqrt_neg25.imag)

# Calculating the square root of -36 is as easy as calculating the sqrt of 36
sqrt_neg36 = 36 ** 0.5 * 1j
print(sqrt_neg36, sqrt_neg36.real, sqrt_neg36.imag)

# We can then operate using these numbers
result = sqrt_neg25 + sqrt_neg36
print(result)  # prints 11j

# We can add regular numbers
result += 7
print(result)  # prints (7+11j)

# and perform regular operations
result *= 3
print(result)  # prints (21+33j)
