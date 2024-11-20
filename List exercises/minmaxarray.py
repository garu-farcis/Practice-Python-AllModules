# Given an array arr. Your task is to find the minimum and maximum elements in the array.
#
# Note: Return an array that contains two elements the first one will be a minimum element and
# the second will be a maximum of an array.
# Input: arr = [3, 2, 1, 56, 10000, 167]
# Output: 1 10000
# Explanation: minimum and maximum elements of array are 1 and 10000.
def minmax():
    arr= [3, 2, 1, 56, 10000, 167]
    val1 =max(arr)
    print("max",val1)
    val2 = min(arr)
    print("min",val2)

minmax()

