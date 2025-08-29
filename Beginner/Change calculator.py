bill = int(input("Total bill: $" ))
user_pays = int(input("User pays: $"))
change = user_pays - bill
if user_pays < bill:
    print("Review user payment")
else:
    print("Return change")
if change % 10 == 9:
    print("Round and return change")
elif change % 10 == 1:
    print("Offer toffee")