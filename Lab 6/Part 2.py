"""
Student: Griffin Gowdey.
Instructor: Dorothy Harman.
Class Number: ITSE1479-20234
Class Name: Intro to Scripting Languages.
Semester: Fall 2020.
Part 2.

Assignment:
Write a GUI program that implements the tax calculator below.

See the "Tax Calculator" PDF for a picture of it.

The window should have a title of “Tax Calculator”. Move the Total 
Tax line up above the Compute Button. Add a Clear button, so the user 
can reset the values. Both the Compute button and Clear button should 
be at the bottom.

The program will have two inputs text areas and radio buttons for 
selecting filing status. It will calculate the total tax using these 
inputs. Default values for the fields should be zero.

The number of dependents should hold a maximum of 2 digits.
Each dependent is a $2,000 deduction. Calculate the dependent credit 
(number of dependents multiplied by 2,000) and create a text area to 
display the result of the calculation.

Add radio buttons for filing status. The overall label will be “Filing 
Status”. Then each radio button will have a label and display the percent 
next to it. The user selects one of these options to determine the tax 
rate. The single option’s rate is 20%. The Married option’s rate is 15%. 
The Divorced option is 10%. The default option is Single is selected.

Calculate the dependent amount by multiplying the number of dependents 
by $2,000.

After you deduct the total dependents amount from gross pay, then multiply 
the remainder by the appropriate status percentage. Display the amount of 
the tax in a line after the Dependents label and box and after the radio 
buttons. Give this line the label of Computed Tax. If you decide to show 
Computed Tax as a textbox, then you will need to disable the box so the 
user can’t enter anything in it.  

Total tax will now display the result of the subtraction of the computed 
dependent amount and computed filing status amount from Gross Income.

You may improve the User Interface any way you please as long as the above 
components are included.

Pseudocode:
Constant: Tax rate/filing status (20%, 15%, or 10%), standard deduction ($12,400), 
and deduction per dependent ($2,000).
Input: Gross income, number of dependents, and filing status.
Process: Equations for net income and income/total tax.
Output: Income/total tax.
"""

# Constant Initialization.
TaxRate = 0.20
StandardDeduction = 12400.0
DependentDeduction = 2000.0

from breezypythongui import EasyFrame
from tkinter import Radiobutton

class TaxCalculator (EasyFrame):

    def __init__ (self):
        EasyFrame.__init__ (self, title = "Tax Calculator")

        # Creating Gross Income label and field.
        self.addLabel (text = "Gross Income", row = 0, column = 0)
        self.incomeField = self.addFloatField (value = 0.0, row = 0, column = 1)

        # Creating Dependents label and field.
        self.addLabel (text = "Dependents", row = 1, column = 0)
        self.depField = self.addIntegerField (value = 0, row = 1, column = 1)

        # Creating Filing Status label and field.
        self.addLabel (text = "Filing Status", row = 2, column = 0)
        self.depField = self.addFloatField (value = 0, row = 2, column = 1)
        
        # Creating radio button for Filing Status.
        t = TaxRate()
        t.set(20)
        Radiobutton (root, text = "Single", variable = t, value = .2).grid(row = 1, column = 3)
        Radiobutton (root, text= "Married", variable = t, value = .15).grid(row = 2, column = 3)
        Radiobutton (root, text= "Divorced", variable = t, value = .1).grid(row = 3, column = 3) 

        # Creating compute button.
        self.addButton (text = "Compute", row = 3, column = 0, columnspan = 3, command = self.computeTax)

        # Creating Total tax label and field.
        self.addLabel (text = "Total tax", row = 4, column = 0)
        self.taxField = self.addFloatField (value = 0.0, row = 4, column = 1, precision = 2)

    # Equations to solve for Total tax.
    def computeTax (self):
        income = self.incomeField.getNumber()
        numDependents = self.depField.getNumber()
        tax = ((income - StandardDeduction - numDependents*DependentDeduction) * TaxRate)
        self.taxField.setNumber (tax)

def main():
    TaxCalculator().mainloop()

if __name__ == '__main__':
    main()