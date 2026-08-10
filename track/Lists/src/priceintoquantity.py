def display_invoice_total(price,quantity):
    total=price*quantity
    if total > 1000:
        print("Total amount is greater than 1000")
    else:
        print("Total amount is less than 1000")
    print(f"The total amount is: {total}")
price=int(input("Enter the price"))
quantity=int(input("Enter the quantity"))
display_invoice_total(price,quantity)