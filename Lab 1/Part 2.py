"""
Student: Griffin Gowdey.
Instructor: Dorothy Harman.
Class Number: ITSE1479-20234
Class Name: Intro to Scripting Languages.
Semester: Fall 2020.
Part 2.

Assignment:
Create a program that prints out a message addressed
to the user that tells them when they'll turn 100 years old.

Pseudocode: 
Input: Import current date and time for future year 
calculation. String for username and int for age.
Process: Store user input of first name, last name, and age.
Equation for what year the user will turn 100.
Outputs: Print line with user's name and the year they'll turn 100.
"""

# Import current date and time for future year calculation.
from datetime import datetime

# User enters their name.
Name = input ("Enter your first and last name: ")

# User enters their age in number format.
Age = int (input ("Enter your age in number format: "))

# Equation for what year the user will turn 100.
Fyear = int ((100-Age) + datetime.now().year) 

# Display message with name and year the user will turn 100.
print ("Hi " + Name + ", you will be 100 years old in the year " + str(Fyear) + ".")