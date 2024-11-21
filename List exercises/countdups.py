# Count occurrences of an element in a list
def countdups(lst):
    mylst=[]
    myset=set()
    freq=0
    for char in lst:
        if char not in myset:
            mylst.append(char)
            myset.add(char)
        else:
            freq= freq+1
            print(char)
    print(freq)

lst=[1,2,3,4,5,5,6,6,7,7,7,7]
countdups(lst)