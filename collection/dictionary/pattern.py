pattern="ABCDBCA"
dict={}
for i in pattern:
    if(i not in dict):
        dict[i]=1
    else:
        print("first recursive character",i)
        break