#import statements
import os
import time
import math
#functions


def find_length(side_lengths): #function to find known lengths

  #Variables for this function
  number_of_sides = 1
  sides = ["hypotenuse","adjasent","opposite"]

  #loops until it ahs asked what all the values are
  while 0 < number_of_sides <= 3:
    #asking what the length of the sides are
    print("What is the length of " + sides[number_of_sides - 1] + "? \nIf the side is unknown please enter '0'")

    #using try to check to make sure that if they enter a letter/word instead of a number
    try:
      #getting user input
      last_entered_length = float(input("Please enter value here: "))
      #if they entered a valid number (not a negitive number or letter/word)
      if last_entered_length >= 0:
        #inputing their input into list
        side_lengths[number_of_sides - 1] = (last_entered_length) 
        #so that it doesnt loop to many times and so it will ask for the next type of side
        number_of_sides += 1
        print()
      else:
        #printing a error message if the value is less than 0
        print("\nError: Please enter a valid number")
    #if they enter a letter/word insead of a number and if the program runs into an error
    except:
      print("\nError: Please enter a valid number")

  #to check if they enered atleast 1 value for length
  if side_lengths.count(0) == 3:
    os.system('clear') #Clears screen
    print("Error: no values entered")
    find_length(side_lengths)

  #making sure they didnt enter an equilateral triangle
  if side_lengths[0] == side_lengths[1] == side_lengths[2]:
    os.system('clear') #Clears screen
    #print error message
    print("Error: Can not have all lengths be the same value")
    find_length(side_lengths)
    
  os.system('clear') #Clears screen
  return side_lengths;


def find_angles(angle_values, side_lengths): #function to find known angles
  
  #Variables for this function
  angles = ["adjasent","opposite"]
  number_known_angles = 1
  #looping untill it has asked what all the values are
  while 0 < number_known_angles <= 2:
    #asking what the values of the angles are
    print("What is the value of the " + angles[number_known_angles - 1] + " angle? \nIf the angle is unknown please enter '0' \nDo not enter the 90° angle.")
    #using try to check to make sure that if they enter a letter/word instead of a number
    try:
      #getting user input
      last_entered_angle = float(input("Please enter value here in degrees: "))
      #checking to make sure the entered value is a valid value
      if 0 <= last_entered_angle < 90:
        #inputing their input into list
        angle_values[number_known_angles] = (last_entered_angle) 
        #so that it doesnt loop to many times and so it will ask for the next angle
        number_known_angles += 1
        print()
      #if they didnt enter a valid value (more than 90, less than 0)
      else:
        print("\nError: Please enter a valid angle")
    #catching errors
    except:
      print("\nError: Please enter a valid angle")

  #if they entered all the values checking to make sure the add up to 180
  if angle_values[0] != 0 and angle_values[1] != 0 and angle_values[2] != 0:
    #math
    if angle_values[0] + angle_values[1] + angle_values[2] != 180: 
      #printing error message
      print("Error: all angles do not add up to 180°\n     This includes the already known 90° angle")
    else:
      return angle_values;
  #if they dont know 1 angle 
  elif angle_values.count(0) == 1:
    return angle_values;

  elif angle_values.count(0) == 0 and side_lengths.count(0) == 1:
    os.system('clear') #Clears screen
    print("Error: only 1 value entered")
    find_length(side_lengths)
    

   
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
  #version: 1.2
  #creator: Daniel Prangnell
  
  #Getting known length values
  
  side_lengths = [0,0,0]
  
  find_length(side_lengths)
  
  #Getting known angle values
  angle_values = [90,0,0]

  find_angles(angle_values)


  #length values put into thier own values
  length_hypotenuse = side_lengths[0]
  length_adjacent = side_lengths[1]
  length_opposite = side_lengths[2]
  
  #angles in degrees
  angle_hypotenuse = 90
  angle_adjacent = angle_values[1]
  angle_opposite = angle_values[2]

  #angles in radians
  angle_adjacent_radians = math.radians(angle_values[1])
  angle_opposite_radians = math.radians(angle_values[2])
  angle_hypotenuse_radians = math.pi / 2 #90° angle

#Date of Creation:05/08/2022
#purpose: to find the lengths and angles using math
#version: 1.0
#creator: Daniel Prangnell
  angle_calculations = "unfinshed"
  
    #calculations (lengths)
  if side_lengths.count(0) == 1:
    if length_hypotenuse == 0:
      length_hypotenuse = round(math.sqrt(math.pow(length_adjacent, 2) + math.pow(length_opposite, 2)),2)
    elif length_adjacent == 0:
      length_adjacent = round(math.sqrt(math.pow(length_hypotenuse, 2) - math.pow(length_opposite, 2)), 2)
    elif length_opposite == 0:
      length_opposite = round(math.sqrt(math.pow(length_hypotenuse, 2) - math.pow(length_adjacent, 2)), 2)
    
  if side_lengths.count(0) == 2:
    if length_hypotenuse == 0:
      print("thing")




  
    #Calculations (angles)
  while angle_calculations != "finished":
    
    
    

    
    if angle_adjacent == 0 and angle_opposite != 0:
      angle_adjacent = 90 - angle_opposite
      angle_adjacent_radians = math.radians(angle_adjacent)
      angle_adjacent_found = True
      
    elif angle_opposite == 0 and angle_adjacent != 0:
      angle_opposite = 90 - angle_adjacent
      angle_opposite_radians = math.radians(angle_opposite)
      angle_opposite_found = True

    if angle_adjacent == 0 and angle_opposite == 0:
      angle_adjacent_radians = math.asin(length_opposite / length_hypotenuse)
      angle_opposite_radians = math.acos(length_adjacent / length_hypotenuse)
      angle_adjacent = math.d
      
      angle_adjacent_found = True
      angle_opposite_found = True
      
      
    print(angle_adjacent)
    print(angle_opposite)
    print(angle_hypotenuse)
    print(length_hypotenuse)
    print(length_adjacent)
    print(length_opposite)
    break
    
  #show user all values
  
  #store values in external txt file
        
  #repeat
  loop = input("do you wish to do another?").lower()
  if loop == "yes" or loop == "y":
    continue
  else:
    break

  
#show all previous values


