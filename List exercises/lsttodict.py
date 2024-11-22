#Python – Convert List to List of dictionaries
# Given list values and keys list,
# convert these values to key value pairs in form of list of dictionaries.dictionaries
# Input : test_list = [“Gfg”, 3, “is”, 8], key_list = [“name”, “id”]
# Output : [{‘name’: ‘Gfg’, ‘id’: 3}, {‘name’: ‘is’, ‘id’: 8}]
# Explanation : Values mapped by custom key, “name” -> “Gfg”, “id” -> 3.


def listtodict():
    lst=['priyanka','is','dodo']
    keyvalues=['word','word1','word2']
    mydict=[]
    ln=len(lst)
    for i in range (0,ln,1):
        mydict.append({keyvalues[i]:lst[i]})
    print(mydict)

listtodict()
