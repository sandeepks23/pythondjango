total=int(input("enter total classes held"))
attended=int(input("enter classes attended"))
percentage=(attended/total)*100
print("percentage of class attended",percentage)
if(percentage<75):
    print("not allowed to attend exam")
else:
    print("allowed to attend exam")                                