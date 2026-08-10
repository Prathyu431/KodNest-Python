seats=[
    "Available",
    "Booked",
    "Available",
    "Available",
    "Booked",
    "Available",
    "Booked",
    "Available"
]
for i in range(len(seats)):
    print("Seat",i+1,":", seats[i])
seat_number=int(input("Enter seat number:"))
if seats[seat_number-1]=="Available":
    seats[seat_number-1]="Booked"
    print("Seat booked successfully")
else:
    print("Seat is already booked")
booked_seats=seats.count("Booked")
available_seats=seats.count("Available")
print("Total Seats:", len(seats))
print("Booked Seats:", booked_seats)
print("Available Seats:", available_seats)
'''
Output:
Seat 1: Available
Seat 2: Booked
Seat 3: Available
Seat 4: Available
Seat 5: Booked
Seat 6: Available
Seat 7: Booked
Seat 8: Available
Enter seat number:
2
Seat is already booked
Total Seats: 8
Booked Seats: 3
Available Seats: 5
'''