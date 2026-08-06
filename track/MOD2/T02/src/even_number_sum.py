limit=int(input("enter the number:"))
number=1
total=0
while number<=limit:
    if number%2==0:
        total=total+number
    number=number+1
print(f"The sum of even numbers is: {total}")