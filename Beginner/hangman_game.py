import random
words = ["cat", "dog", "lion", "tiger", "zebra", "monkey", "panda", "rabbit","apple", "banana", "mango", "grape", "orange", "cherry", "peach", "lemon","anna", "mark", "lucy", "john", "emma", "liam", "noah", "mia", "oliver", "ava","book", "chair", "table", "watch", "pizza", "guitar", "pencil", "phone","sun", "moon", "star", "cloud", "rain", "snow", "tree", "flower", "grass","car", "bike", "train", "plane", "boat", "ship", "house", "door", "window"]
stages = [
"""
  +---+
      |
      |
      |
     ===
""",
"""
  +---+
  O   |
      |
      |
     ===
""",
"""
  +---+
  O   |
  |   |
      |
     ===
""",
"""
  +---+
  O   |
 /|   |
      |
     ===
""",
"""
  +---+
  O   |
 /|\\  |
      |
     ===
""",
"""
  +---+
  O   |
 /|\\  |
 /    |
     ===
""",
"""
  +---+
  O   |
 /|\\  |
 / \\  |
     ===
"""
]
placeholder = ""    #picks a random word from the words list and prints dashes,
life = 6
wrong_guesses = 0
word = random.choice(words)
guessed_letters = []

word_length = len(word)
for index in range(word_length):
    placeholder += "_"

placeholder_list = list(placeholder)
word_count = list(word)

print(word)
print(placeholder)

while word_count != placeholder_list and life>0:
    user_guess = input("Guess the letter to save the hangman: \n").lower()
    if user_guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    else:
        guessed_letters.append(user_guess)
    if user_guess in word_count:
        for i in range(len(word_count)):
            if word_count[i] == user_guess:
                placeholder_list[i] = user_guess
        print(' '.join(placeholder_list))
    else:
        life -= 1
        wrong_guesses += 1
        print(f"{' '.join(placeholder_list)}, \nIncorrect letter! Remaining lives: , {life}, \n{stages[wrong_guesses]}")

if word_count == placeholder_list and life>0:
    print("You win!")
else:
    print("You lose!")