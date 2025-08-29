print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? : S, M, or L ")
pepperoni = input("Do you want pepperoni on your pizza? Type Y for yes or N for No ")
cheese = input("Do you want cheese on your pizza? Type Y for yes and N for No ")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill +=3

if cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}.")