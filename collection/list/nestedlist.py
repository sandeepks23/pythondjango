employee=[[1001,"arun",15000],
          [1002,"arjun",20000],
          [1003,"vijay",25000],
          [1004,"binu",10000]]
sum=0
for i in employee:
    if(i[2]>17000):
        print(i[1])
    sum=sum+i[2]
print(sum)