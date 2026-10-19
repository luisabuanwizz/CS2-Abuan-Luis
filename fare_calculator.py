# Travel Fare Calculator
FARE_RATE = 14

name = input("Enter passenger name: ")
if name == "":
    print("Name should not be left empty. Please try again.")
    name = input("Enter passenger name: ")

distance = float(input("Enter distance (km): "))
if distance <= 0:
    print("Distance should be greater than 0. Please try again.")
    distance = float(input("Enter distance (km): "))

try:
 passengers = int(input("Enter number of passengers: "))
 if passengers <= 0:
    print("Amount of passengers should be a positive whole number. Please try again")
    passengers = int(input("Enter number of passengers: "))
except ValueError:
 print("Amount of passengers should be a positive whole number. Please try again")
 passengers = int(input("Enter number of passengers: "))

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))

# Validation rules
# 1. Passenger name -- Must not be empty
# 2. Distance -- Number greater than 0
# 3. Passengers -- Positive whole number