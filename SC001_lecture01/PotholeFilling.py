"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def turn_right():
    for i in range(3):
        turn_left()


def put_99():
    for i in range(99):
        put_beeper()


def turn_around():
    turn_left()
    turn_left()


def go_in():
    move()
    turn_right()
    move()


def go_out():
    turn_around()
    move()
    turn_right()
    move()


def main():
    """
    Howard:
    """
    for i in range(3):
        go_in()
        put_99()
        go_out()



# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
