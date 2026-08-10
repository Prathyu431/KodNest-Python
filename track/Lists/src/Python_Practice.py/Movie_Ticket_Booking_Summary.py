#Movie ticket booking summary
#customer name
#age
#number of tickets
customer_name=input("Enter customer name: ")
age=int(input("Enter age: "))
number_of_tickets=int(input("Enter number of tickets: "))
if age<12:
    ticket_price=120
elif age<=59:
    ticket_price=200
else:
    ticket_price=150
total_before_discount=ticket_price*number_of_tickets
if number_of_tickets>=5:
    discount=total_before_discount*0.1
else:
    discount=0
total_after_discount=total_before_discount-discount
print("\n--- Movie Ticket Booking Summary ---")
print(f"Customer Name: {customer_name}")
print(f"Age: {age}")
print(f"Number of Tickets: {number_of_tickets}")
print(f"Ticket Price: {ticket_price}")
print(f"Total Before Discount: {total_before_discount}")
print(f"Discount: {discount}")
print(f"Total After Discount: {total_after_discount}")