values=[10,10,20,20,20,30,10,10,40]
result=[]
for value in values:
    if len(result)==0 or result[-1]!=value:
        result.append(value)
print("Original List:")
print(values)
print("Result:")
print(result)
'''
Output:
Original List:
[10, 10, 20, 20, 20, 30, 10, 10, 40]
Result:
[10, 20, 30, 10, 40]
'''
