alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
process = input("Type ENCRYPT to encrypt your message or type DECRYPT to decrypt received message: \n").lower()
user_text = input("Type your text: \n").lower()
shift = int(input("Type the shift amount: \n"))

def caesar(text, shifted_amount, direction):
    output_text = ""
    if direction == "decode":
        shifted_amount *= -1
    for letters in text:
            shifted_position = alphabets.index(letters) + shifted_amount
            shifted_position %= len(alphabets)
            output_text += alphabets[shifted_position]
    print(output_text)

caesar(text=user_text, shifted_amount=shift,direction=process)