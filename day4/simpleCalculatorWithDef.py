import myModule
a=(int(input("Enter Number1: ")))
b=(int(input("Enter Number2: ")))
operator=input("enter the operator: ")
try:
    
   if operator in ("+","add","addition"):
    myModule.add(a,b)
   elif operator in ('-',"sub","substraction"):
    myModule.sub(a,b)
   elif operator in ('*','mul','Multiplication'):
    myModule.mul(a,b)
   elif operator in ('/',"div","division"):
    myModule.div(a,b)
   else:
    print("invalid operator")
except ZeroDivisionError:
    print("You cannot divide by Zero")