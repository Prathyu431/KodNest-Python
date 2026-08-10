message=input("Enter the message:")
print("First 5 Characters:",message[:5])
print("Last 5 Characters:",message[-5:])
print("Character from Index 2 to 7",message[2:8])
print("Every Second Character:",message[::2])
print("Message int Reverse:",message[::-1])
print("Message Without First and Last:",message[1:-1])

'''
Output:
Enter the message:
Hello World
First 5 Characters: Hello
Last 5 Characters: World
Character from Index 2 to 7 llo Wo
Every Second Character: HloWrd
Messafe int Reverse: dlroW olleH
Message Without First and Last: ello Worl
'''