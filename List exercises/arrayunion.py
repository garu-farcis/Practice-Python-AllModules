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
    for i in range(len(b)):
        c.append(b[i])
    #removing duplicates from c
    final_lst=[]
    freq=set()
    for i in c:
       if i not in freq:
           final_lst.append(i)
           freq.add(i)
    print(final_lst)

unionarray()





