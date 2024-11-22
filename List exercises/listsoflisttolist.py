# breaking a list of list into a list aka flattening
def change():
    lst =[['hello',' world'],['converting','list'],['oflist','todict']]
    mynewlst=[]
    n =len(lst)
    for i in lst:
        for element in i:
            print(element)
            mynewlst.append(element)
            print(mynewlst)
change()