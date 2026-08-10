text=input("Enter text:")
uppercase=0
lowercase=0
digit=0
spaces=0
others=0
for ch in text:
    if ch.isupper():
        uppercase=uppercase+1
    elif ch.islower():
        lowercase=lowercase+1
    elif ch.isdigit():
        digit=digit+1
    elif ch.isspace():
        spaces=spaces+1
    else:
        others=others+1
print(f"Uppercase: {uppercase}")
print(f"Lowercase: {lowercase}")
print(f"Digits: {digit}")
print(f"Spaces: {spaces}")
print(f"Others: {others}")
'''
Output:
Enter text:
Hello World 123!
Uppercase: 2
Lowercase: 8
Digits: 3
Spaces: 2
Others: 1
'''