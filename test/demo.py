try:
    a=int(input("enter a"))
except Exception as e:
    print(e.args)
