#import statements
import os
import time
import math
#functions


def find_length(): #function to find lengths

  #Variables for this function
  number_of_sides = 1
  side_lengths = [0,0,0]
  while 0 < number_of_sides <= 3:
    print("What is the length of side " + str(number_of_sides) + "? \nIf the side is unknown please enter '0'")
    #print(side_lengths + " " + last_entered_length)
    try:
      last_entered_length = int(input("Please enter value here: "))
      if last_entered_length >= 0:
        side_lengths[number_of_sides - 1] = (last_entered_length) 
        number_of_sides += 1
        print()
        
    except:
      print("\nError: Please enter a valid intiger")
  
  #return side_lengths
#---------------Main Routine----------------

#Date of Creation:28/07/2022
#purpose: to welcome the user
#version: 1.0
#creator: Daniel Prangnell


print("Welcome to this right angle triangle calculator V1.0")

print("This is designed to make your homework easier.")
input("Press Enter to begin:")
time.sleep(2) #Adds 2 second pause
os.system('clear') #Clears screen
exit_code = ""
while exit_code != "xxx":

  #Date of Creation:28/07/2022
  #purpose: to find the lengths and angles
  #version: 1.0
  #creator: Daniel Prangnell
  
  #Getting known length values
  length_1 = 0
  length_2 = 0
  length_3 = 0
  find_length()
  
  #Getting known aqngle values
  angle_1 = 0
  angle_2 = 0
  angle_3 = math.pi / 2 #90° angle
  
  #calculations (lengths)
  
  #Calculations (angles)
  
  #show user all values
  
  #store values in external txt file
  
  #repeat
  break

  
#show all previous values
  