#Parking Fee Calculator
#Write a python program that calculate the parking charges based on the number of hours a vehicle stays in the parking lot.
#Assume that the first 2 hours are free and the subsequent hours are charged at Rs. 50 per hour.
#Your program should ask for the number of hours the vehicle stayed and print the parking charges.
hours=int(input("Enter parking hours:"))
if hours<=2:
    parking_charges=hours*30
elif hours>=3 and hours<=5:
    parking_charges=hours*25
else:
    parking_charges=hours*20
if parking_charges>150:
    service_charges=20
else:
    service_charges=0
total_charges=parking_charges+service_charges
print(f"Parking Charge: {parking_charges}")
print(f"Service Charges: {service_charges}")
print(f"Total Charge: {total_charges}")


'''
parking charges:
1-2 hours 30 rupees
3-5 hours 25 rupees
6-10 hours 20 rupees
'''
# Output:
# Enter parking hours:
# 4
# 100
# Parking Charge: 120
# Service Charges: 100
# Total Charge: 320
