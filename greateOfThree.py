a,b,c= map(int ,input("Enter 3 Number:").split(","))
if a>b:
    if a>c:
        print("A is greater")
    elif c>a:
        print("C is greater")
    else:
        print("A and C is Eqaul")
elif b>a:
    if b>c:
        print("B is greater")
    elif c>b:
        print("C is greater")
    else:
        print("B and C is Eqaul")
else:
    print("A,B,C is eqaul")