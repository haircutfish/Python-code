#!/bin/python3

from datetime import datetime #Time Stamp
import socket #Connecting to target IP
import os #Used to clear the screen
import time #Timing the scanner
import sys

os.system('cls' if os.name == 'nt' else 'clear') #Clear the screen

print("""
                /\                                  /\              
               |  \                                /  |                  
               |    \            / \             /    |          
               |     \      /\  /   \  / \      /     |           
               |       \ ^ /  \/     \/   \ ^ /       | 
               |                                      |      
               /                                       \                
              /            \                /           \             
             /            | \              / |           \        
            /             |  \            /  |            \           
           /              |  @\          /@  |             \          
          /               |    \        /    |              \        
         /                 \___/        \___/                \       
        /                                                     \            
       /               |\______________________/|              \         
      /      \         |   |   |   |   |   |    |        /\     \        
     /      / \        |   |   |   |   |   |    |       /  \     \    
    /      /   \       |   |   |   |   |   |    |      /    \     \      
   /      /     \       \  |   |   |   |   |   /      /      \     \     
  /      \       \       \_|___|___|___|___|__/      /       /      \  
   \/\/\/        /\                                 /\        \/\/\/  
                /  \                               /  \               
               |                                       |       
               |         \____________________/        |      
                \          |              |          /       
                <_________/                \_________>    	""")



HOST = input("Gengar needs to know what IP address you want to scan?  ") or 0 #User inputs IP address
if HOST == 0:
    print ('-'*60) #Banner
    print("You didn't enter a host to scan, Gengar sulks back to the shadows :(")
    print ('-'*60) #Banner
    sys.exit()
    
print ('-'*60) #Banner

inputports = input('Gengar needs to know how many ports you want to scan? ') or 0 #User inputs how many Ports to scan
if inputports == 0:
    print ('-'*60) #Banner
    print("You didn't enter any ports to scan, Gengar sulks back to the shadows :( ")
    print ('-'*60) #Banner
    sys.exit()
prts = int(inputports)


print ('-'*60) #Banner

print('Gengar uses shadow ball to scan {}'.format(HOST)) #Fluff and show what IP you are scanning

t1 = time.time() #Timer

print ('-'*60)#Banner

print('Scan started at: ', datetime.now()) #Time stamp of start of scan


for PORT in range(0,prts): #Loop through Ports of IP address
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Socket used for Host and TCP connection 
		s.connect((HOST,PORT)) #The actual connection to the target IP
		print('Port {} is open'.format(PORT)) #Print out what ports are open
		

	except:
		pass 

print ('-'*60) #Banner

print('Scan done at: ', datetime.now()) #Time stamp of end of scan

t2 = time.time()#Timer

tend = t2 - t1 #Calculating how long it took to scan

print ('-'*60) #Banner

print(f'It took this {tend} for shadowball to scan your system.') #Showing how long it took to scan 
	