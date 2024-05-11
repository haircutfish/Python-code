
#Hash Comparer
import sys

hashone = input("Please input first hash: ") or 0
if hashone == 0:
	print("You didn't input a hash.")
	print("Exiting program")
	sys.exit()

hashtwo = input('Please input second hash: ') or 0
if hashtwo == 0:
	print("You didn't input a hash.")
	print("Exiting program")
	sys.exit()

if hashone == hashtwo:
		print('This file is safe to use!')

else:
	print('Do not open, may have been compromised')