#Program to find sum and average of List in Python
import math
from os import lseek


def avgsum(lst):
    myval=[]
    sum=0
    for i in lst:
        sum += i
    avg= float(sum/len(lst))
    print('sum',sum)
    print('avg',avg)

lst=[1,2,3,4,5]
avgsum(lst)
