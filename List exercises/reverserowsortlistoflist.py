# to perform the sorting of rows of the matrix in descending order

def mysort():
    lst=[[4,6,5],[1,2,3]]
    newlst=[]
    rownum=[0,1]
    lst.sort()
    print(lst)
    for i in lst:
        i.sort(reverse=True)

    print(lst)

mysort()