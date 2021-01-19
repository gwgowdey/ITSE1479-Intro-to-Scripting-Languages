"""
Student: Griffin Gowdey.
Instructor: Dorothy Harman.
Class Number: ITSE1479-20234
Class Name: Intro to Scripting Languages.
Semester: Fall 2020.
Part 1.

Assignment:
Open the file MorseCode.py, look at the structure, save the file to your 
local machine, and answer the following questions.

1.) Write the statement to import the dictionary.
2.)	Write the statement to find out how long the dictionary is.
3.)	Write the statement to find out if the lowercase a is in the list.
4.)	Write the statement to find out if the uppercase A is in the list.
5.)	Write the statement to find out if lowercase a is not in the list.
6.)	Write the statement to find out what the _name_ is.

Use this link for help if needed: 
https://www.python-course.eu/python3_dictionaries.php
"""

# 1a.) Importing morsecode.py file after saving file to local machine.
import MorseCode

# 1b.) Importing dictionary as morse from morsecode.py.
from MorseCode import morse

# 2.) Finding out how long the dictionary is.
dict_size = len (morse)

# 3.) Finding out if the lowercase a is in the list.
print ('a' in morse)

# 4.) Finding out if the uppercase A is in the list.
print ('A' in morse)

# 5.) Finding out if lowercase a is not in the list.
print ("a" not in morse)

# 6.) Finding out what the_name_is.
print ("Results from morsecode.py file")