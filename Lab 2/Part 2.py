"""
Student: Griffin Gowdey.
Instructor: Dorothy Harman.
Class Number: ITSE1479-20234
Class Name: Intro to Scripting Languages.
Semester: Fall 2020.
Part 2.

Assignment:
The credit plan at TidBit Computer Store specifies a 10% down payment 
and an annual interest rate of 12%. Monthly payments are 5% of the listed 
purchase price, minus the down payment. Write a program that takes the 
purchase price as input. The program should display a table, with 
appropriate headers, of a payment schedule for the lifetime of the loan. 
Each row of the table should contain the following items:

•	The month number (beginning with a 1)
•	The current total balance owed
•	The interest owed for that month
•	The amount of principal owed for that month
•	The payment for that month
•	The balance remaining after payment

Pseudocode:
Input: Float for purchase price.
Processes: Equations for price after initial down payment, monthly
payment of 5% of the listed total/purchase price minus the down 
payment, interest owed for the respective month, and principal for 
the respective month. While loop and equation to solve problem.
Output: Print numbers for the table.
"""

# User inputs the total/purchase price of item.
PurchasePrice =  float (input ("Enter the total/purchase price of item: "))

# Equation for price after initial down payment.
RemainingPrice = (PurchasePrice * 0.9)

# Equation for monthly payment of 5% of the listed total/purchase price, minus the down payment.
MonthlyPayment = (RemainingPrice * 0.05)

# Equation for interest owed for the respective month.
InterestOwed = (RemainingPrice * (.12/12.0))

# Equation for principal for the respective month.
Principal = (MonthlyPayment - InterestOwed)

# Month count for loop.
Month = 0

# Output/printing numbers for the table.
print ("%0d Months%20.2f%20.3f%20.2f%13.2f%23.2f" %(Month, PurchasePrice, InterestOwed, Principal, MonthlyPayment, RemainingPrice))

# Loop/equation to solve problem.
while RemainingPrice > 0:
    Month += 1
    RemainingPrice -= Principal
    InterestOwed = (RemainingPrice * (.12/12.0))
    Principal = (MonthlyPayment - InterestOwed)

    # Printing numbers for the table.
    print ("%0d Months%20.2f%20.3f%20.2f%13.2f%23.2f" %(Month, PurchasePrice, InterestOwed, Principal, MonthlyPayment, RemainingPrice))