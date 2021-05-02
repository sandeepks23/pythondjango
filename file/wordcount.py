f=open("data","r")
dict={}
for lines in f:
    word=lines.rstrip("\n").split(" ")
for i in word:
    if(i not in dict):
        dict[i]=1
    else:
        dict[i]+=1
print(dict)