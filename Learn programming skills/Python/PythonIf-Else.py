

import math
import os
import random
import re
import sys

n = random.randint(1, 100)  # Random integer between 1 and 100
n=4
print(n)
odd = n % 2 != 0
print(odd)
even = n % 2 == 0
print("even",even)

if odd:
    print("Weird")
elif even >= 2 and even <= 5:
    print("Not Weird")


# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of  to , print Not Weird
# If n is even and in the inclusive range of  to , print Weird
# If n is even and greater than , print Not Weird
# Input Format
