# Given two arrays a[] and b[], the task is to find the number of elements in the union between these two arrays.
#
# The Union of the two arrays can be defined as the set containing distinct elements from both arrays.
# If there are repetitions, then only one element occurrence should be there in the union.
#
# Note: Elements are not necessarily distinct.
# Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3]
# Output: 5
# Explanation: 1, 2, 3, 4 and 5 are the elements which comes in the union set of both arrays. So count is 5.

def unionarray():
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3]
    c= []
    for i in range(len(a)):
        c.append(a[i])

    print(c)

unionarray()





