"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def up():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()


def cross():
    move()
    turn_right()


def down():
    while front_is_clear():
        move()
    turn_left()


def jump():
    up()
    cross()
    down()


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()








# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
