print("select an operation to perform")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
print("---------------------------------------")

operation=input()
if operation=="1":
    num1=input("Enter first number:")
    num2=input("Enter second number:")
    print("The sum is "+str(float(num1)+float(num2)))
elif operation=="2":
    num1=input("Enter first number:")
    num2=input("Enter second number:")
    print("The subtraction is "+str(float(num1)-float(num2)))
elif operation=="3":
    num1=input("Enter first number:")
    num2=input("Enter second number:")
    print("The multiplication is "+str(float(num1)*float(num2)))
elif operation=="4":
    num1=input("Enter first number:")
    num2=input("Enter second number:")
    print("The division is "+str(float(num1)/float(num2)))
else:
    print("Invalid Entry")
    


