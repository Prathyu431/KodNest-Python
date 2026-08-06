n=int(input("Enter the number:"))
total=0
pc=0
nc=0
zc=0
for i in range(n):
    num=int(input())
    total=total+num
    if num>0:
        pc=pc+1
    elif num<0:
        nc=nc+1
    else:
        zc=zc+1
print(f"Positive count: {pc}")
print(f"Negative count: {nc}")
print(f"Zero count: {zc}")
print(f"Total: {total}")    