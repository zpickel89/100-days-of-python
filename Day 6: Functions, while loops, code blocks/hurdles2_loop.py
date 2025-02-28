"""These are provided by the exercise, added to remove errors outside of that"""
def move():
    return
def turn_left():
    return
def at_goal():
    return

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    jump_hurdle()

