a = int(input("Enter first number: "))
b = int(input("Enter second number: ")) 

print("1 for Addition")
print("2 for Subtraction")
print("3 for Multiplication")
print("4 for Division") 

value=int(input("What do you want to perform: "))

# Addition and subtraction use return to send the result back.
# Multiplication and division print the result directly.
# This program demonstrates both approaches.

def addition(a,b):
    sum=a+b
    return sum

def subtraction(a,b):
    sub=a-b
    return sub

def multiplication(a,b):
    mult=a*b
    print("Multiplication is: ",mult)

def division(a,b):
    if b == 0:
        print("Cannot divide by Zero")
    else:
        div=a/b
        print("Division is: ",div)

if value == 1:
    s = addition(a,b)
    print("Addition is: ",s)
elif value == 2:
    s1 = subtraction(a,b)
    print("Subtraction is: ",s1)
elif value == 3:
    multiplication(a,b)
elif value == 4:
    division(a,b)
else:
    print("Invalid Input")