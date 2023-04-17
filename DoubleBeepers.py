"""
File: DoubleBeepers.py
Name:
-------------------------------
TODO:
"""

from karel.stanfordkarel import *


def turn_back():
    turn_left()
    turn_left()


def put_back():
    move()
    while on_beeper():
        pick_beeper()
        turn_back()
        move()
        put_beeper()
        turn_back()
        move()


def double():
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        turn_back()
        move()
        turn_back()


def main():
    """
    Karel will double the beepers
    """
    move()
    while on_beeper():
        double()
    put_back()
    turn_back()
    move()
    move()
    turn_back()




# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
