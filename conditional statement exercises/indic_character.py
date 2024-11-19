# Welcome to the part 2 of For Loops in Python. In this question, we'll learn to print
# characters of a string at even indices.
# You are given a string str, you need to print its characters at even indices(index starts at 0).
# Note: Please go through the range function to understand how to jump 2 steps.
def altindices():
    mystr = input("Enter your string ")
    for i in range(0,len(mystr),2):
        print(mystr[i])

altindices()