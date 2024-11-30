# Input:
# str = hello
# x = llo
# Output:
# hello
# 2
# Hello
# HELLO

def inbuiltfuncs():
    str= 'Hello'
    strcaps= str.upper()
    strtrim =str.strip('He')
    strcount=len(str)
    strswap =str.swapcase()
    strfind=str.find('l')
    strsub =str.isalpha()

    print(strcaps,strtrim,strcount,strsub,strfind,strswap,sep=' ',end='\n')

inbuiltfuncs()