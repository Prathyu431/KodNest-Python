limit=int(input("Enter the limit:"))
target=int(input("Enter the target:"))
count=0
total=0
found=False
for i in range(1,limit+1):
    if i%3==0:
        count=count+1
        total=total+i
        if i==target:
            found=True
            break
print(f"Count: {count}")
print(f"Total: {total}")
if found==True:
    print("Target Found: Yes")
else:
    print("Target Found: No")   