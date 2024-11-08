# This is my first microbit code
# jingle bells notes in a forever loop

from microbit import * 
import music

jingle_bells = ['e','e','e',  # "Jingle Bells"
         'r',                 # Pause/Rest
         'e','e','e',         # "Jingle Bells"
         'r',                 # Pause/Rest
         'e','g','c','d','e', # "Jingle All The Way"
         'r',                 # Pause/Rest
         'f','f','f','f','e','e','e','e','d','d','e','r','d', #"Oh, what fun it is to ride in a one-horse open sleigh,"
         'r',                 # Pause/Rest
         'g',                 # "Hey!" 
         'r',]                # Pause/Rest

while True:
    music.play(jingle_bells)