#lst=[1,3,11,4,22]
#def square(num1):
#    return num1**2
#squ=list(map(square,lst))
#print(squ)

lst=[1,3,11,4,22]
squ=list(map(lambda n:n**2,lst))
print(squ)

cubes=list(map(lambda num:num**3,lst))
print(cubes)


