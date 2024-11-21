
def remvedups(lst):
    mylst=[]
    myset=set()
    for char in lst:
        if char not in myset:
            mylst.append(char)
            myset.add(char)
    print(mylst)

lst=[]
length = int(input("enter the no of elements for the list"))
for i in range(0,length):
    element = int(input())
    lst.append(element)
remvedups(lst)
