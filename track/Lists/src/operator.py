def calculator(first_number,second_number,operator):
    if operator=='+':
        return first_number+second_number
    elif operator=='-':
        return first_number-second_number
    elif operator=='*':
        return first_number*second_number
    elif operator=='/':
        return first_number/second_number
    else:
        return "Invalid operator"
operator=input("enter operator")
first_number=int(input("enter first number"))
second_number=int(input("enter second number"))
result=calculator(first_number,second_number,operator)
print(result)