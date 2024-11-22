#convert a list of lists into a dictionary

def convert():
    lst =[['hello',' world'],['converting','list'],['oflist','todict']]
    keyval =['word','word1','word2']
    length= len(lst)
    x=dict(lst)
    print(x)
    mydict=[]
    for i in range(0,length,1):
        mydict.append({keyval[i]:lst[i]})
    print(mydict)

convert()

