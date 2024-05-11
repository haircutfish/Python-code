# Following the YouTube Video by Kari, I created this fun game from an old 
# 80s Usborne Computer Coding Book
# https://www.youtube.com/watch?v=3kdM9wyglnw
# https://drive.google.com/file/d/0Bxv0SsvibDMTVUExUjFhTURCSU0/view?resourcekey=0-v2liG0G60g8b7DXjJtDBXg

import os
import random
import string
import time

# Clear Screen
os.system('cls||clear')

# Initial Message
print('VITAL MESSAGE')
print('\n')

# Asking the difficulty
while True:
    difficulty = int(input('HOW DIFFICULT? (4-10)\n'))
    if difficulty >= 4 and difficulty <= 10:
        break

# Lop to create the message
message = ''

for i in range(difficulty):
    message += random.choice(string.ascii_uppercase)

# Clear Screen
os.system('cls||clear')

# Message displayed
print('SEND THIS MESSAGE:\n')

print(message)

# Clear screen after determined amount of seconds
time.sleep(0.5*difficulty)

os.system('cls||clear')

# Attempt to write the message

attempt = input('').upper()

# Check attempt against message
if attempt == message:
    print('MESSAGE CORRECT\nTHE WAR IS OVER')
else:
    print('YOU GOT IT WRONG\nYOU SHOULD HAVE SENT:')
    print(message)
