#Accepts two user inputs from user and then accept operation (+,-,*,/) according to the operation provided execute the neccessary operation
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
operation=input("Enter the operation (+,-,*,/):")
if(operation=="+"):
    print(num1+num2)
elif(operation=="-"):
    print(num1-num2)
elif(operation=="*"):
    print(num1*num2)
elif(operation=="/"):
    print(num1/num2)
else:
    print("Invalid operation")