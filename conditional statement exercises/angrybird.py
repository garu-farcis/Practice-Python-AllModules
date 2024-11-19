#You are familiar with basics of input/output and many other useful things in Python.
# This module is all about conditional statements like if, elif, else; for, while, etc.
#
# In Python, any conditional statement ends with ':'
# (proper indentation must be followed while working through loops).
#
# There are two friends, John and Smith, and the parameters j_angry and s_angry to indicate if each is angry. You are
# in trouble if both of them are angry or no one of them is angry.
#
# Now, complete the function which returns true if you are in trouble, else return false
def checkstatus():
    j_angry = input("Is john in angry.Enter y/n?")
    s_angry = input("Is john in angry.Enter y/n?")
    if j_angry==s_angry== 'y':
        print("I am in trouble")
        flag = True
    elif j_angry== s_angry== 'n':
        print("I am not in trouble")
        flag= False
    else:
        print(" unsure")
        flag = False
    return flag

checkstatus()

