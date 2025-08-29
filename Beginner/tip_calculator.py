print ("Welcome to the tip calculator!")

#stores total bill
total_bill = float(input("What was the total bill? \n$"))

#stores tip percentage
offered_tip = float(input("How much tip would you like to give?\n"))

#stores the number of people the bill will split into
split_bill = float(input("How many people to split the bill?\n"))

#calculate total payment per person
total_tip = (offered_tip/100) * total_bill
bill_per_person = (round((total_tip + total_bill) / split_bill,2))

#print the tip for all people
print (f"Each person should pay: ${bill_per_person:.2f}")