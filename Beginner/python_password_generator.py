import random

alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
specials = ["!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}",";",":","'",'"',",",".","<",">","/","?","\\","|"]
Password = []

print("Welcome to Python Password Generator")
alphabet_length = int(input("How many letters do you want in your password?: "))
number_length = int(input("How many numbers do you want in your password?: "))
special_length = int(input("How many special characters do you want in your password?: "))

for pw_alphabet in range(alphabet_length):
    random_alphabets = random.choice(alphabets)
    Password.append(random_alphabets)

for pw_number in range(number_length):
    random_numbers = random.choice(numbers)
    Password.append(random_numbers)

for pw_special in range(special_length):
    random_specials = random.choice(specials)
    Password.append(random_specials)

random.shuffle(Password)
print("".join(Password))