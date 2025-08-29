alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input("Type your text: \n").lower()
shift = int(input("Type the shift amount: \n"))

list_of_text = list(text)

def encrypt(original_text,shift_amount):
    for i in alphabets:
        if list_of_text in alphabets:
            list_of_text[i] = shift

encrypt(text,shift)
print(list_of_text)