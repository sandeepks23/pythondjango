line="hai hello hai hello hai"
print(line)
word=line.split(" ")
print(word)
dict={}
for i in word:
    if(i not in dict):
        dict[i]=1
    else:
        dict[i]+=1
print(dict)

