# You are given a string str, you need to return True if  the words "cat" and "hat"
# appear same number of times in
# str, otherwise return False. Note: str contains only lowercase English alphabets.
def checkstr():
    mystr =input("enter a string")
    matches= ['cat','hat']
    # we use any iterable for finding any of the matches, we can use all iterable
    # for making sure all vales in matches are present
    if any(x in mystr for x in matches):
        print('present')
        return True
    else:
        return False
checkstr()