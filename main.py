#import statements
import os
import time
import math
#functions


def find_length(side_lengths): #function to find known lengths

  #Variables for this function
  number_of_sides = 1
  sides = ["hypostenuse","adjasent","opposite"]
  while 0 < number_of_sides <= 3:
    print("What is the length of " + sides[1 - number_of_sides] + "? \nIf the side is unknown please enter '0'")

    try:
      last_entered_length = float(input("Please enter value here: "))
      if last_entered_length >= 0:
        side_lengths[number_of_sides - 1] = (last_entered_length) 
        number_of_sides += 1
        print()
    except:
      print("\nError: Please enter a valid number")
  
  if side_lengths[0] == 0 and side_lengths[1] == 0 and side_lengths[2] == 0:
    os.system('clear') #Clears screen
    print("\nError: no values entered")
    find_length(side_lengths)
  return side_lengths;


def find_angles(angle_values): #function to find known angles

  #Variables for this function
  number_known_angles = 1
  while 0 < number_known_angles <= 2:
    print("What is the value of angle " + str(number_known_angles) + "? \nIf the angle is unknown please enter '0' \nDo not enter the 90° angle.")
    try:
      last_entered_angle = float(input("Please enter value here in degrees: "))
      if 0 <= last_entered_angle < 90:
        angle_values[number_known_angles] = (last_entered_angle) 
        number_known_angles += 1
        print()
      else:
        print("\nPlease enter a valid angle")
    except:
      print("\nError: Please enter a valid angle")
  print(angle_values)

  if value
  if angle_values[0] + angle_values[1] + angle_values[2] != 180: 
    print("Error: all angles do not add up to 180°")
  return angle_values;

   
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
  #version: 1.1
  #creator: Daniel Prangnell
  
  #Getting known length values
  length_1 = 0
  length_2 = 0
  length_3 = 0
  side_lengths = [0,0,0]
  
  find_length(side_lengths)
  print(side_lengths)
  #Getting known angle values
  angle_1 = 0
  angle_2 = 0
  angle_3 = math.pi / 2 #90° angle
  angle_values = [90,0,0]
  find_angles(angle_values)
  #calculations (lengths)
  
  #Calculations (angles)
  
  #show user all values
  
  #store values in external txt file
  
  #repeat
  break

  
#show all previous values
  