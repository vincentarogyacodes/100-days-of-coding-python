print('''
                         .-.
                         '-'
                        //
               _..---._/|
             .' ."     `-.
            /__/          \      *
           ====_____     __|     :
          /#   #""" |   /()\    :    ..*
          |#   #    |   \__/    : .'' 
          \#___#____|      /   :*:.. .
           \______________|_...f_: .. '*
  ()       // /\||||))))))):::::::   . .
 .( \_     \\_\//   _-'.'/::M-K:::|   * ..
( )  |^|^|^|ooo/  _#\.//"""_::::::|   . . .
(_)_.'v|v|v|     / \#  \_ / `_:::'    . .
           | _ _/_/     /`./_-\"         . .
           /#_#__"""-._ /#  \__)       .  .   
           |__   ""-._ |##               . . .
           |  ""|-"""-_/##              . .    
           /""--\__.-|                       .
           \-_.-<__ /                   .   .
           /-_| /  \
           \-_| \_-<.                        .  .
           <_-/ <_.-\                    .
           <_-|  |_.-|                        .
      .----|   \__\  |                 .
     |     ."""   `.  |                       .
      .___|        |__|
          `.__..."""  
''')


print("Welcome to Treasure Island! Your mission is to find the treasure!")

starting_direction = input("Which direction do you want to go? Type Left or Right ")
if starting_direction == "Right" or starting_direction == "right":
    print("You encounter a Golem and got torn to shreds, Game Over!")
    exit()
if starting_direction == "Left" or starting_direction == "left":
    second_action = input("You reach a large door, do you want to open it? Types Yes or No ")
if second_action == "Yes" or second_action == "yes":
    print("A catapult was flung at you, game over!")
    exit()
if second_action == "No" or second_action == "no":
    aiding_men = input("Three men come to aid you, who do you follow? Type Man 1, Man 2, or Man 3 ")
if aiding_men == "Man 2" or "man 2":
    print("The man takes you to the treasure! You won!")
else:
    print("Game Over!")