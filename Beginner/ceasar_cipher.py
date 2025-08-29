alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cipher = []
text = input("Type your text: \n").lower()
shift = int(input("Type the shift amount: \n"))

list_of_text = list(text)

# def encrypt(original_text,shift_amount):
for i in text:
    if i in alphabets:
        cipher = alphabets.index(i) + shift
        print(cipher)