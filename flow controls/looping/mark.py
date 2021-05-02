sub1=float(input("enter sub1 mark"))
sub2=float(input("enter sub2 mark"))
sub3=float(input("enter sub3 mark"))
sub4=float(input("enter sub4 mark"))

sum=sub1+sub2+sub3+sub4
percentage=(sum/200)*100
if(percentage>=90):
    print("Grade is A+")
elif((percentage>=80)&(percentage<89)):
    print("Grade is A")
elif((percentage>=70)&(percentage<79)):
    print("Grade is B+")
elif((percentage>=60)&(percentage<69)):
    print("Grade is B")
elif((percentage>=50)&(percentage<59)):
    print("Grade is C+")
elif((percentage>=40)&(percentage<49)):
    print("Grade is C")
elif((percentage>=30)&(percentage<39)):
    print("Grade is D+")
else:
    print("Fail")
