"""
Student: Griffin Gowdey.
Instructor: Dorothy Harman.
Class Number: ITSE1479-20234
Class Name: Intro to Scripting Languages.
Semester: Fall 2020.
Part 3.

Assignment:
An employee’s gross weekly pay equals their hourly wage multiplied 
by the total number of regular hours plus any overtime pay. Overtime 
pay equals the total overtime hours multiplied by 1.5 times the hourly 
wage. Write a program that takes as inputs the hourly wage, total regular 
hours, and total overtime hours and displays an employee’s gross weekly 
pay. Note:  we are not going to take into consideration taxes. We are 
calculating gross pay only. Be sure that you display appropriate prompts 
for input so the viewer knows what to type in.  And make sure that your 
output is identified as: Weekly Gross Pay.

Pseudocode:
Input: Float for regular hours, overtime hours, and hourly wage.
Process: Equation for calculating weekly gross pay.
Output: Weekly gross pay.
"""

# User enters the number of regular hours worked.
RegularHours = float (input ("Enter your number of regular hours worked in whole number or decimal format (max of 40.0): "))

# User enters the number of overtime hours worked.
OvertimeHours = float (input ("Enter your number of overtime hours worked in whole number or decimal format: "))

# User enters the hourly wage of that employee.
HourlyWage = float (input ("Enter your hourly wage in whole number or decimal format: "))

# Display equation for user to calculate Weekly Gross Pay.
print ("Weekly Gross Pay = (regular hours worked x your hourly wage) + (overtime hours x (1.5 x your hourly wage))")

# Equation for calculating Weekly Gross Pay.
print ("Employee weekly gross pay = ")
print ((RegularHours * HourlyWage) + (OvertimeHours * (1.5 * HourlyWage)))