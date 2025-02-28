"""https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json"""

"""These are provided by the exercise, added to remove errors outside of that"""
def move():
    return
def turn_left():
    return
def at_goal():
    return
def wall_in_front():
    return
def wall_on_right():
    return
def front_is_clear():
    return
def right_is_clear():
    return
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
turn_left()
 
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()