# The original list is : [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
# The list after pairing is : [[[4, 6], [5, 6]], [[2, 5], [4, 5]], [[6, 5], [7, 5]]]

# Python3 code to demonstrate
# Pair elements with Rear element in Matrix Row
# using product() + loop
from itertools import product
def pairing():
    mylst = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
    flatlst=[]
    # flattening it into a single list to create new pairs
    # for i in mylst:
    #     for element in i:
    #         flatlst.append(element)
    # print('flattened list', flatlst)
    #or using product from itertools to create a product of the first and the rear element
    for i in mylst:
        flatlst.append(list(product(i[:-1],[i[0]])))

    print(flatlst)


pairing()