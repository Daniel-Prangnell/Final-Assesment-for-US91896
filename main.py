#import statements
import os
import time
import math
import sys

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
      last_entered_length = float(input("Please enter value here:"))
      #if they entered a valid number (not a negitive number or letter/word)
      if last_entered_length >= 0:
        if side_lengths[0] < side_lengths[1] and side_lengths[0] < side_lengths[2]:
          print("Error: The hypotenuse should be the longest length")
          continue
        else:
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
  angles = ["adjacent","opposite"]
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
    #testing to make sure if they entered all that it adds up to 180°
    if angle_values[0] + angle_values[1] + angle_values[2] != 180: 
      #printing error message
      os.system('clear') #Clears screen
      print("Error: all angles do not add up to 180° \n(This includes the already known 90° angle) \n")
      find_angles(angle_values, side_lengths)
    else:
      return angle_values;
  #if they dont know 1 angle 
  elif angle_values.count(0) == 1:
    return angle_values;

  #if they entered every value for the triangle
  if angle_values.count(0) == 0 and side_lengths.count(0) == 0:
    os.system('clear') #Clears screen
    print("Error: all values entered \n")
    do_another(do_another_triangle)


def do_another(do_another_triangle):
  do_another_triangle = input("do you wish to do another? ").lower()
  return do_another_triangle
   
#---------------Main Routine----------------
#to clear the history file  
with open("history.txt",'w') as file:
    pass

#Date of Creation:28/07/2022
#purpose: to welcome the user
#version: 1.0.1
#creator: Daniel Prangnell

print("Welcome to this right angle triangle calculator V1.0")

print("This is designed to make your homework easier.")
input("Press Enter to begin:")
time.sleep(2) #Adds 2 second pause
os.system('clear') #Clears screen

number_of_loops = 1 #variable to keep track of how many triangle the user has entered


while True:

  #Date of Creation:28/07/2022
  #purpose: to find the lengths and angles
  #version: 1.3
  #creator: Daniel Prangnell
  
  #Getting known length values

  #variables
  angle_values = [90,0,0]
  side_lengths = [0,0,0]
  two_values_entered = False
  
  while two_values_entered == False: #looping
    
    find_length(side_lengths)
    
    #Getting known angle values
    
    find_angles(angle_values, side_lengths)
    #if one or no lengths are unknown
    if side_lengths.count(0) <= 1:
      two_values_entered = True
    #if one length is known and one angle (other than the 90° angle) is known
    elif side_lengths.count(0) == 2 and angle_values.count(0) == 1:
      two_values_entered = True

    else:
      os.system('clear') #Clears screen
      print("Error: only 1 value entered \n")



  #length values put into thier own values
  length_hypotenuse = side_lengths[0]
  length_adjacent = side_lengths[1]
  length_opposite = side_lengths[2]
  
  #angles in degrees
  angle_hypotenuse = 90
  angle_adjacent = angle_values[1]
  angle_opposite = angle_values[2]

  #angles in radians
  angle_adjacent_radians = math.radians(angle_values[1]) #making the values radians
  angle_opposite_radians = math.radians(angle_values[2]) #making the values radians
  angle_hypotenuse_radians = math.pi / 2 #90° angle

  
  #Date of Creation: 05/08/2022
  #purpose: to find the lengths and angles using math
  #version: 1.0
  #creator: Daniel Prangnell
  
  while angle_values.count(0) != 0 and side_lengths.count(0) != 0:
    
    #*********************calculations (lengths)*********************
    
    if side_lengths.count(0) == 1: #to see whether there is only one unknown length
      if length_hypotenuse == 0: #to see if the hypotenuse is the unknown length
        #A² + B² = C²
        length_hypotenuse = round(math.sqrt(math.pow(length_adjacent, 2) + math.pow(length_opposite, 2)),2)
        side_lengths[0] = length_hypotenuse #asigning the value to the list
      elif length_adjacent == 0:  #to see if the adjacent is the unknown length
        #A² = C² - B²
        length_adjacent = round(math.sqrt(math.pow(length_hypotenuse, 2) - math.pow(length_opposite, 2)), 2)
        side_lengths[1] = length_adjacent #asigning the value to the list
      elif length_opposite == 0:  #to see if the opposite is the unknown length
        #B² = C² - A²
        length_opposite = round(math.sqrt(math.pow(length_hypotenuse, 2) - math.pow(length_adjacent, 2)), 2)
        side_lengths[2] = length_opposite #asigning the value to the list
      
    if side_lengths.count(0) == 2: #to see whether there is 2 unknown lengths
      
      if length_adjacent == 0 and angle_adjacent != 0: #see if the adjacent length is unknown and is the adjacent angle is known
        if length_hypotenuse != 0: #see if the hypotenuse length is known
          length_adjacent = round(math.cos(angle_adjacent_radians) * length_hypotenuse, 2) #calculation for adjacent length using adjacent angle and the hypotenuse length
        if length_opposite != 0: #see if the opposite length is known
          length_adjacent = round(math.tan(angle_adjacent_radians) * length_opposite, 2) #calculation for adjacent length using adjacent angle and the opposite length
        side_lengths[1] = length_adjacent #putting value in list

        
      elif length_opposite == 0 and angle_opposite != 0: #see if the oppostie length is unknown and is the opposite angle is known
        if length_hypotenuse != 0: #see if the hypotenuse length is known
          length_opposite = round(math.sin(angle_opposite_radians) * length_hypotenuse, 2) #calculation for opposite length using adjacent angle and the hypotenuse length
        if length_adjacent != 0: #see if the adjacent length is known
          length_opposite = round(math.tan(angle_opposite_radians) * length_adjacent, 2) #calculation for opposite length using adjacent angle and the adjacent length
        side_lengths[2] = length_opposite #putting value in list
  
  
      
    
      #*********************Calculations (angles)*********************
        
    if angle_adjacent == 0 and angle_opposite != 0: #if the adjacent angle is unknown and opposite angle is known
      angle_adjacent = round(90 - angle_opposite, 2) #calculation: angle 1 = 180 - angle 2 - angle 3
      angle_adjacent_radians = math.radians(angle_adjacent) #Making angle into radian
      side_lengths[1] = length_adjacent #putting value in list
      
    if angle_opposite == 0 and angle_adjacent != 0: #if the opposite angle is unknown and adjacent angle is known
      angle_opposite = round(90 - angle_adjacent, 2) #calculation: angle 1 = 180 - angle 2 - angle 3
      angle_opposite_radians = math.radians(angle_opposite) #Making angle into radian
      side_lengths[2] = length_opposite #putting value in list
  
    if angle_adjacent == 0 and angle_opposite == 0 and length_opposite != 0 and length_hypotenuse != 0:
      angle_adjacent_radians = math.asin(length_opposite / length_hypotenuse) #calculation: Soh Cah Toa
      angle_opposite_radians = math.acos(length_opposite / length_hypotenuse) #calculation: Soh Cah Toa
      angle_adjacent = round(math.degrees(angle_adjacent_radians), 2) #Making angle into a radian
      angle_opposite = round(math.degrees(angle_opposite_radians), 2) #Making angle into a radian
      side_lengths[1] = length_adjacent #putting value in list
      side_lengths[2] = length_opposite #putting value in list
      
    elif angle_adjacent == 0 and angle_opposite == 0 and length_adjacent != 0 and length_hypotenuse != 0:
      angle_adjacent_radians = math.asin(length_adjacent / length_hypotenuse) #calculation: Soh Cah Toa
      angle_opposite_radians = math.acos(length_adjacent / length_hypotenuse) #calculation: Soh Cah Toa
      angle_adjacent = round(math.degrees(angle_adjacent_radians), 2) #Making angle into a radian
      angle_opposite = round(math.degrees(angle_opposite_radians), 2) #Making angle into a radian
      side_lengths[1] = length_adjacent #putting value in list
      side_lengths[2] = length_opposite #putting value in list
  
    elif angle_adjacent == 0 and angle_opposite == 0 and length_adjacent != 0 and length_opposite != 0:
      angle_adjacent_radians = math.asin(length_opposite / length_adjacent) #calculation: Soh Cah Toa
      angle_opposite_radians = math.acos(length_opposite / length_adjacent) #calculation: Soh Cah Toa
      angle_adjacent = round(math.degrees(angle_adjacent_radians), 2) #Making angle into a radian
      angle_opposite = round(math.degrees(angle_opposite_radians), 2) #Making angle into a radian
      side_lengths[1] = length_adjacent #putting value in list
      side_lengths[2] = length_opposite #putting value in list
    
  #show user all values
  os.system('clear') #Clears screen
  print("The adjacent angle is " + str(angle_adjacent) + "°")
  print("The opposite angle is " + str(angle_opposite) + "°")
  print("The hypotenuse angle is " + str(angle_hypotenuse) + "°")
  print("The hypotenuse length is " + str(length_hypotenuse))
  print("The adjacent length is " + str(length_adjacent))
  print("The opposite length is " + str(length_opposite))
    
    
  #Date of Creation: 18/08/2022
  #purpose: store triangle values to a txt file so it can be saved for later
  #version: 1.0
  #creator: Daniel Prangnell
  
  #store values in external txt file. already formated
  save_file = open("history.txt", "a")
  save_file.write("Triangle " + str(number_of_loops) + " sizes: \n")
  save_file.write("The adjacent angle is " + str(angle_adjacent) + "°\n")
  save_file.write("The opposite angle is " + str(angle_opposite) + "°\n")
  save_file.write("The hypotenuse angle is " + str(angle_hypotenuse) + "°\n")
  save_file.write("The hypotenuse length is " + str(length_hypotenuse) + "\n")
  save_file.write("The adjacent length is " + str(length_adjacent) + "\n")
  save_file.write("The opposite length is " + str(length_opposite) + "\n\n")
  save_file.close()
  

  #Date of Creation: 16/08/2022
  #purpose: to find if the user wants to to another triangle
  #version: 1.0
  #creator: Daniel Prangnell

  #if they want to do another triangle
  do_another_triangle = "no"
  do_another_triangle = do_another(do_another_triangle)
  if do_another_triangle == "y" or do_another_triangle == "yes":
    number_of_loops += 1
    os.system('clear') #Clears screen
    continue
  else:
    os.system('clear') #Clears screen
    break

  
#show all previous values
    
while True:
  show_previous_values = input("Do you wsh to see your previous triangles from this session? ")
  
  if show_previous_values == "y" or show_previous_values == "yes":
    save_file = open("history.txt", "r")
    print(save_file.read())
    save_file.close()
    break
  
  elif show_previous_values == "no" or show_previous_values == "n":
    break
    
  else:
    print("please enter yes or no")