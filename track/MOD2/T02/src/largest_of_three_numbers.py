num1=int(input("Enter the number1:"))
num2=int(input("Enter the number2:"))
num3=int(input("Enter the number3:"))

if(num1>num2 and num1>num3):
    print(f"Number is largest:{num1}")
elif(num2>num1 and num2>num3):
    print(f"Number is largest:{num2}")
elif(num3>num1 and num3>num2):
    print(f"Number is largest:{num3}")  