import random
rock = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissor = '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player = input("Choose 0 for rock, 1 for paper, and 2 for scissor")
choices = [rock, paper, scissor]
if player == "0":
    print(f"You chose\n{rock}")
elif player == "1":
    print(f"You chose\n{paper}")
elif player == "2":
    print(f"You chose\n{scissor}")
computer = random.choice(choices)
print(f"Computer Chose\n{computer}")

if computer == rock and player == "0":
    print("Draw!")
elif computer == paper and player == "1":
    print("Draw!")
elif computer == scissor and player == "2":
    print("Draw!")
elif computer == rock and player == "1":
    print("You Win!")
elif computer == paper and player == "2":
    print("You Win!")
elif computer == scissor and player == "1":
    print("You Win!")
elif computer == rock and player == "2":
    print("You Lose!")
elif computer == paper and player == "0":
    print("You Lose!")
elif computer == scissor and player == "1":
    print("You Lose")