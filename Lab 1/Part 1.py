"""
Student: Griffin Gowdey.
Instructor: Dorothy Harman.
Class Number: ITSE1479-20234
Class Name: Intro to Scripting Languages.
Semester: Fall 2020.
Part 1.

Assignment:
Create a program that prints the user's name and age. Display
both name and age in a full sentence.

Pseudocode:
Input: String for user's first and last name and int for age.
Process: Store user input of first name, last name, and age.
Output: Print line with user's name and age.
"""

# User enters their first and last name.
Name = input ("Enter your first and last name: ")

# User enters their age in number format.
Age = int (input ("Enter your age in number format: "))

# Display message with name and age.
print (Name + " is " + str(Age) + " years old.")