# Now you are familiar with While loop in Python.
# Let's get deeper into understanding it through below question.
#
# Given a positive integer x,
# the task is to print the numbers from 1 to x in the order as 1^2, 2^2, 3^2, 4^2, 5^2, ... (in increasing order).
import math
def jumpwhile():
    num = int(input("enter any positive integer"))
    x=1
    val =1
    while x< num:
        x = math.pow(val,2)
        if val<num:
            if x<num:
                val = val + 1
                print(x)
            else:
                return False
        else:
            return False


jumpwhile()