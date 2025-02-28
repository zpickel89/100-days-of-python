"""https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json"""

"""These are provided by the exercise, added to remove errors outside of that"""
def move():
    return
def turn_left():
    return
def at_goal():
    return
def wall_in_front():
    return

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump_hurdle()
    else:
        move()
