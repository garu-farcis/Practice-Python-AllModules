# Given a list of lists. The task is to extract a random element from it.
# Input : test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]
# Output : 7
# Explanation : Random number extracted from Matrix.

import numpy as np
import random

mylist= [[1,2,3],[4,5,8],[4,5,6],[0,1,7]]
row_num=[1,2,3,4,0,5]
#converting our list to array. the list shoudl always be homogenous for this to work
myarray= np.array(mylist)
result = np.random.choice(myarray[random.choice(row_num)])
print(result)
