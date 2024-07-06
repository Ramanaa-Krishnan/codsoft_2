#CALCULATOR - TASK 2 - CODSOFT
#basic arithmetic operations by user defined values

def add(a,b):
    print("Performing Addition Operation..!!")
    return a+b

def sub(a,b):
    print("Performing Subtraction Operation..!!")
    return a-b

def mul(a,b):
    print("Performing Multiplication Operation..!!")
    return a*b

def div(a,b):
    try:
        print("Performing Division Operation")
        return a/b
    except ZeroDivisionError:
        print("A value cannot be divided with ZERO..!!")
    
def mdiv(a,b):
    print("Performing Modulo Division Operation..!!")
    return a%b

def exp(a,b):
    print("Performing Exponentiation Operation..!!")
    return a**b

def fdiv(a,b):
    print("Performing Floor Division Operation..!!")
    return a//b

while True:
    
    a=int(input("Enter your first operand : "))
    b=int(input("Enter your second operand : "))
    print("""

1 - ADDITION
2 - SUBTRACTION
3 - MULTIPLICATION
4 - DIVISION
5 - MODULO DIVISION
6 - EXPONENTIAION
7 - FLOOR DIVISION """)
    
    ch=int(input("Enter your integral choice for manipulation : "))
    if ch==1:
        print("The answer is : ",add(a,b))
    elif ch==2:
        print("The answer is : ",sub(a,b))
    elif ch==3:
        print("The answer is : ",mul(a,b))
    elif ch==4:
        print("The answer is : ",div(a,b))
    elif ch==5:
        print("The answer is : ",mdiv(a,b))
    elif ch==6:
        print("The answer is : ",exp(a,b))
    elif ch==7:
        print("The answer is : ",div(a,b))
    else:
        raise(ValueError("Entered a Invalid Operator..Please Try Again..!!"))


    con=int(input("Enter 1 to continue and 0 to break : "))
    if con:
        pass
    else:
        break
