# Given a natural number n,
# the task is to write a Python program to first find the sum of first n natural numbers
# and then print each step as a pattern.
#
#
#     Input: 5
#
#     Output:
#
#     1 = 1
#     1 + 2 = 3
#     1 + 2 + 3 = 6
#     1 + 2 + 3 + 4 = 10
#     1 + 2 + 3 + 4 + 5 = 15

def natural_nums():
    num = int(input("enter your number"))
    # mylim = int(input("enter your limit"))
    val =0
    for i in range(num):
        val= val+ i
        i= i+1
        print(val)
natural_nums()