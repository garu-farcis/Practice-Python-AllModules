#Writing for loop in Python is a tad different from C++ and Java counterparts.
# In this question, we'll learn to print table by using the for loop.

# You are given a number N, you need to print its multiplication table.
#
# Note: Please go through the range function to understand why it's useful in for loops.
# Syntax : range(start, stop, step)
# Parameters :
# start : Element from which sequence constructed has to start. (default:0)
# stop : Element number at which numbers in sequence have to end (exclusive).
# step : Can be +ve or -ve number, denoting the elements need to be skipped during filling of list. (default:1)
# Returns : The list using the formula :
# list[n] = start + step*n (for both positive and negative step) where, n >=0 and list[n] = 0 and list[n] > stop (for negative step)
# Returns ValueError if step is 0. Value constraint is checked in case of step,
# failing to meet returns empty sequence, else returns sequence according to formula.
def multable():
    num = int(input("enter the number for the multiplication table"))
    for i in range(1,11,1):
        val = num * i
        print(val,'\n')

multable()