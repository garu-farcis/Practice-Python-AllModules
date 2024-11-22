def convert():
    mydict={"word":"hello",
            "word1":"world"}
    print(mydict)
    mylst=[]
    for i in mydict:
        mylst.append(mydict[i])
        print(mylst)

convert()