
# Python program to interchange first and last elements in a list
# Given a list, write a Python program to swap the first and last element of the list using Python.
#
# Examples: The last element of the list can be referred to as a list[-1].
# Therefore, we can simply swap list[0] with list[-1].
def swapele(lst):
    lst[0],lst[-1]=lst[-1],lst[0]
    print(lst)
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

swapele(lst)

def swapusingtemp(lst):
    size= len(lst)
    temp =lst[0]
    lst[0]=lst[size-1]
    lst[size-1]=temp
    print(lst)



swapusingtemp(lst)
