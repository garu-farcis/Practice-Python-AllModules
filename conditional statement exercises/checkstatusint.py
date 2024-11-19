#Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.
# Return True for the following cases:
#
#     Either a or b (not both) is non-negative and the flag is false.
#     Both a and b are negative and the flag is true.
#
# Otherwise, return false.
# Input:
# a = 1
# b = -1
# flag = False
# Output:
# True
# Explanation:
# Since a and b are positive and
# negative respectively and flag
# is False, so return True.
a= int(input("Enter first number"))
b= int(input("Enter second number"))
if a | b >0:
    print("flag=False")
elif(a & b <0):
    print("flag= True")
else:
    print("flag= False ")





