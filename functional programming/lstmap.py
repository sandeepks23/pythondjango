lst=[4,2,1,6,7,8]
res=[]
for i in lst:
    if(i<5):
        i-=1
        res.append(i)
    else:
        i+=1
        res.append(i)
print(res)

result=list(map(lambda num:num-1 if num<5 else num+1,lst))
print(result)