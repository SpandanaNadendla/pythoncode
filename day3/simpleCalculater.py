a=(int(input("Enter Number1: ")))
b=(int(input("Enter Number2: ")))
operator=input("enter the operator: ")

if (operator == ("+","add","addition")):
    print(a+b)
elif (operator == '-',"sub","substraction"):
    print(a-b)
elif (operator == '*'):
    print(a*b)
elif (operator == '/'):
    print(a/b)
else:
    print("invalid operator")
