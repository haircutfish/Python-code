#!/usr/bin/env python3

# Following the YouTube Video by Kari, I created this fun game from an old 
# 80s Usborne Computer Coding Book
# https://www.youtube.com/watch?v=3kdM9wyglnw
# https://drive.google.com/file/d/0Bxv0SsvibDMTVUExUjFhTURCSU0/view?resourcekey=0-v2liG0G60g8b7DXjJtDBXg

import os
from time import sleep
import random
import msvcrt

# Clear the screen
os.system('cls||clear')

# On screen dialogue
print('COWBOY SHOOTOUT -\nYOU ARE BACK TO BACK\nTAKE 10 PACES...')

# On screen paces
paces = 1

td = [0.2, 0.5]

while paces <= 10:
    print(paces,'...')
    paces += 1
    sleep(random.choice(td))

# Waiting for HE Draws
newtd = random.randint(1,3)

sleep(newtd)

print('HE DRAWS')

# "Shooting" or not
x = 0
while x < newtd:
    if msvcrt.kbhit() == True:
        print('BUT YOU SHOOT FIRST.\nYOU KILLED HIM.')
        exit()
    else:
        sleep(0.5)
        x = x + 1

print('AND SHOOTS.\nYOU ARE DEAD')


