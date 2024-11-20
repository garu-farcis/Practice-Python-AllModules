# Given a positive integer N,
# the task is to write a Python program to check if the number is Prime or not in Python.
# A prime number is a number that can only be divided by itself and 1 without remainders
import math

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

print(is_prime(11))  # True
print(is_prime(1))   # False
