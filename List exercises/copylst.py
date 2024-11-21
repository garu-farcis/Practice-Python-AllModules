#Cloning or Copying a list
def clone(lst):
    newlst=[]
    for i in lst:
        newlst.append(i)
    print(newlst)

lst=[1,2,3,4,5,6]
clone(lst)