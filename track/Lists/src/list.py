#function
def check_sign(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
num = int(input("Enter a number: "))
print(check_sign(num))