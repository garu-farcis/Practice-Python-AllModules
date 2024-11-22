# Count occurrences of an element in a list
def countdups(lst):
    mylst=[]
    myset=set()
    myindex=[]
    freq=0
    for char in lst:
        if char not in myset:
            mylst.append(char)
            myset.add(char)
        else:
            freq= freq+1
            print('the repeated values are ',char)
            # myindex.append(char)
            val= lst.index(char)
            print('the index respectively are',val )

    print('frequency is ', freq)

lst=[1,2,3,4,5,5,6,6,7,7,7,7]
countdups(lst)