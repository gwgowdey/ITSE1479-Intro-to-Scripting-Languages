"""
Student: Griffin Gowdey.
Instructor: Dorothy Harman.
Class Number: ITSE1479-20234
Class Name: Intro to Scripting Languages.
Semester: Fall 2020.
Part 1.

Assignment: 
This assignment uses an input file.

The payroll department keeps a list of employee information for 
each pay period in a text file.  The format of each line of the 
file is the following:

<last name> <hourly wage> <hours worked>

You do not know how many employees are listed in the file.
Write a program that inputs a filename from the user (the file is 
supplied in the files for the assignment) and prints a report (to 
the python shell) of the wages paid to the employees for a given period. 
The report should be in tabular format with the appropriate headings. 
Each line should contain an employee’s name, the hours worked, and the 
wages paid for that period.

You will need to set up a test text file with the employee information 
in order to test your program. Include the test data file with your 
upload of your python file. Name the data file: testdata.txt

Pseudocode:
Input: File name as input from the user.
Processes: Opening the file from input and equation for wages paid.
Output: Print the column headers and wages paid to the employees
for a given period.
"""

# Taking filename as input from the user.
FileName = input ("Enter the full file name with extension: ")

# Opening the file with read operation.
fp = open (FileName, "r")

# Printing the headers.
print ("\nLast Name      Hours Worked      Total Paid")

# Using for loop to iterate through the files.
for column in fp.readlines():
    values = column.strip().split()
    
    # Printing the wages paid for each employee from the input file.
    print("s% %d %.2f"%(values[0],int(values[1]),int(values[1])*float(values[2])))

# Closing the file.
fp.close()