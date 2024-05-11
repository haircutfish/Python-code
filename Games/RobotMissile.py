#!/usr/bin/env python3

# Using the Usborne Computer BattleGames from 1982, I first made the game in a BBC virtual console
# From there I created it in python, which is what you see below
# Here are the links to the Virtual Console and the Usborne Digital book
# Virtual Console - BBC - https://virtual.bbcmic.ro/?disc1=elite.ssd&autoboot
# https://drive.google.com/file/d/0Bxv0SsvibDMTVUExUjFhTURCSU0/view?resourcekey=0-v2liG0G60g8b7DXjJtDBXg


import random
import string

# opening display
print('''
      ROBOT MISSILE
      TYPE THE CORRECT CODE
      LETTER (A-Z) TO
      DEFUSE THE MISSILE.
      YOU HAVE 4 CHANCES
      ''')

# selecting random letter and placing in a variable
rando_letter = random.choice(string.ascii_uppercase)

# loop check guesses against random letter
guess = 1

while guess <= 5:
    # user guesses a letter and captilized
    letter_guess = input('?').capitalize()
    # guess is to early in the alphabet
    if letter_guess < rando_letter:
        print('LATER')
    # guess is to late in the alphabet
    elif letter_guess > rando_letter:
        print('EARLIER')
    # guess is correct
    elif letter_guess == rando_letter:
        print('TICK....FZZZZZZ...CLICK...\nYOU DID IT!!!!!')
        break
    # to many wrong guesses, bomb blew up
    if guess == 4:
        print(f'''
BOOOOOOOOOOOOOOMMMMMMMM....
YOU BLEW IT!
THE CORRECT CODE WAS {rando_letter}      
    ''')
        break
    guess += 1