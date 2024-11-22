#This particular article aims at achieving the task of finding uncommon two list,
# in which each element is in itself a list.
# This is also a useful utility as this kind of task can come in life of programmer
# if he is in the world of development.
def checkcommon():
    lst1=[[1,2],[2,3],[3,4],[4,5],5]
    lst2=[[1,2],[5,6],[3,4]]
    uncommonlst=[]
    for i in lst1:
        if i not in lst2:
            uncommonlst.append(i)
    for i in lst2:
        if i not in lst1:
            uncommonlst.append(i)
    print(uncommonlst)

checkcommon()