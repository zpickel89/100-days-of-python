"""
Treasure island exercise
https://viewer.diagrams.net/index.html?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D
"""

print('''
    ___ __ 
   (_  ( . ) )__                  '.    \   :   /    .'
     '(___(_____)      __           '.   \  :  /   .'
                     /. _\            '.  \ : /  .'
                .--.|/_/__      -----____   _  _____-----
_______________''.--o/___  \_______________(_)___________
       ~        /.'o|_o  '.|  ~                   ~   ~
  ~            |/    |_|  ~'         ~
               '  ~  |_|        ~       ~     ~     ~
      ~    ~          |_|O  ~                       ~
             ~     ___|_||_____     ~       ~    ~
   ~    ~      .'':. .|_|A:. ..::''.
             /:.  .:::|_|.\ .:.  :.:\   ~
  ~         :..:. .:. .::..:  .:  ..:.       ~   ~    ~
             \.: .:  :. .: ..:: .lcf/
    ~      ~      ~    ~    ~         ~
               ~           ~    ~   ~             ~
        ~         ~            ~   ~                 ~
   ~                  ~    ~ ~                 ~
''')
print("Welcome to treasure island. Your mission is to find the treasure")
branch_choice = input("You come to a branch on the path will you go \"left\" or \"right\"?")

if branch_choice == "Left" or branch_choice == "left":
    swim_choice = input("When continuing down the path you come across a small river, it looks narrow enough to swim across.  Will you wait or swim? ").lower()
    if swim_choice == "wait":
        door_choice = input("Some large turtles swim by on the river and you are able to hop across the river on the backs of their shells, once safely across the river you encounter 3 doors.  The first door is red, the second is blue and the third is yellow.  You must go through one of these doors which will you choose?")
        if door_choice == "Yellow" or door_choice == "yellow":
            print("You found the treasure you win!")
        elif door_choice in("Red", "red"):
            print("Behind the door there was nothing but a crackling campfire, you didn't find the treasure but time to roast some marshmallows! Game over")
        elif door_choice == "Blue" or door_choice == "blue":
            print("Behind the blue door there is nothing, well that's disappointing.  Game over. You get nothing you lose good day sir!")
        else:
            print("You decide the real treasure is the island itself and go to start building a shelter")
    else:
        print("You decided to swim across but you forgot you didn't know how and drowned... oops.  Game over")
else:
    print("You picked the wrong path and got lost somehow, Game over")