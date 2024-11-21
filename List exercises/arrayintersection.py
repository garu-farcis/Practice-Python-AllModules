# Intersection of two sorted arrays
# Given two sorted arrays arr1[] and arr2[]. Your task is to return the intersection of both arrays.
#
#     Intersection of two arrays is said to be elements that are common in both arrays. The intersection should not count duplicate elements.
#
# Note: If there is no intersection then return an empty array.
# Input: arr1[] = [1, 2, 3, 4], arr2[] = [2, 4, 6, 7, 8]
# Output: [2, 4]
# Explanation: 2 and 4 are only common elements in both the arrays.
def intersection(a,b):
    c=[]
    for char in a:
        if char in b:
            c.append(char)
        elif char not in b:
            print(" ")
    print(c)



a=[1, 2, 3, 4]
b= [2, 4, 6, 7, 8]
intersection(a,b)
