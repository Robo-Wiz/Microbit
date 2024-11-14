
# this program simulates dice rolls

from microbit import *
import random

while True:
    # if button 'a' is pressed then microbit will display a random roll between 1 to 6
    # this simulates roll of one dice
    if button_a.is_pressed():
        dice = random.randint(1,6)
        display.scroll(dice)

    # if button 'b' is pressed then microbit will display a random roll between 1 to 12
    # this simulates roll of two dice together
    elif button_b.is_pressed():
        dice = random.randint(2,12)
        display.scroll(dice)
