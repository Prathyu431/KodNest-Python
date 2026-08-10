#Multiplication Table Generator & Pattern Analyzer
n=int(input("Enter a number:"))
even_count=0
odd_count=0
for i in range(1,11):
    result=n*i
    if result%2==0:
        status="Even"
        even_count=even_count+1
    else:
        status="Odd"
        odd_count=odd_count+1
    print(f"{n}*{i}={result} - {status}")
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
'''
Output:
Enter a number:
5
5*1=5 - Odd
5*2=10 - Even
5*3=15 - Odd
5*4=20 - Even
5*5=25 - Odd
5*6=30 - Even
5*7=35 - Odd
5*8=40 - Even
5*9=45 - Odd
5*10=50 - Even
Even numbers: 5
Odd numbers: 5
'''