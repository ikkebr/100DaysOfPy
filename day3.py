#!/usr/bin/env python3

days = 7
hours = 24
minutes = 60

seconds_in_a_week = days * hours * minutes
seconds_in_two_weeks = 2 * seconds_in_a_week

days = days + 7  # days is now 14
days += 7  # days is now 21 (14 + 7)
days *= 2  # days is now 42 (21 * 2)
days -= 32  # days is now 10 (42 - 32)
days //= 2  # days is now 5 (10 // 2) - // is integer division
days /= 1  # days is now 5.0 ( 5 / 1 ) - / is float division
days %= 3  # days is now 2.0 (5.0 % 3)

print(days)  # prints 2.0