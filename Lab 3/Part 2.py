"""
Student: Griffin Gowdey.
Instructor: Dorothy Harman.
Class Number: ITSE1479-20234
Class Name: Intro to Scripting Languages.
Semester: Fall 2020.
Part 2.

Assignment:
This assignment creates an output file.

Write a program to create a new text file. Name the text file data2.txt. 
The program will write 10 lines to the file. Each line will say “This 
is line number x”, where x is a number from 1 to 10 (have a counter that 
the program will increment) and place the counter in the line before writing 
to the file. Basically, you are creating line numbers. Be sure to add a 
carriage return and a new line character at the end of each line.
Verify that the file was created after your program runs.

The output should look like this:
This is line number 1
This is line number 2
This is line number 3
And so on.

Now modify your program to read the file data2.txt and print the contents 
of the file to the Python Shell.

Pseudocode:
Input: Data file name with extension.
Process: Loop to create number of 1 to 10 for each line 
and the name of each line in the file.
Output: Opening and closing the file.
"""

# Opening the file data2.txt in append+ mode to create file and append data.
DataFile = open ('data2.txt', 'a+')

# Looping from x 1 to 10.
for x in range (1, 10):
    
    # Creating a line named "This is line number x" and starting a new line.
    DataFile.write ('This is line number ' + str(x) + '\n')

# Closing the file.
DataFile.close()

# Opening the file data2.txt in read mode.
DataFile = open ('data2.txt', 'r')

# Looping through all lines in the file.
for line in DataFile.readlines():
    print (line)

# Closing the file.
DataFile.close()