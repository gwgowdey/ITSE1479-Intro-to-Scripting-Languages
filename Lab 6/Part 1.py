"""
Student: Griffin Gowdey.
Instructor: Dorothy Harman.
Class Number: ITSE1479-20234
Class Name: Intro to Scripting Languages.
Semester: Fall 2020.
Part 1.

Assignment:
Write a GUI-based program that allows the user to convert temperature values 
between degrees Fahrenheit and degrees Celsius. The interface should have 
labeled entry fields for these two values. These components should be arranged 
in a grid where the labels occupy the first row and the corresponding fields 
occupy the second row. At start-up, the Fahrenheit field should contain 32.0 
and the Celsius field should contain 0.0. The third row in the window contains 
two command buttons, labeled “Convert to Celsius” and “Convert to Fahrenheit”. 
When the user presses the first button, the program should use the data in the 
Fahrenheit field to compute the Celsius value, which should then be output to 
the Celsius field. The second button should take the Celsius value and convert 
it to Fahrenheit and display the answer in the Fahrenheit field.

Extra Credit:
Change the background color of the window from white to gray (or another color).
The text labels for Celsius and Fahrenheit should be a dark blue (or a good contrasting 
color for the background you have chosen). The window should have a title of “Temperature 
Conversion”. You may improve on the user interface any way you please.

Pseudocode:
Input: Degrees Fahrenheit and degrees Celsius.
Process: Equation to convert between the two
temperature types.
Output: Converted temperature.
"""

# First class.
class First:

    # Converting temperature from Celsius to Fahrenheit.
    def convertToFahrenheit (self, celsius):
        return (celsius * (9/5)) + 32
 
    # Converting temperature from Fahrenheit to Celsius.
    def convertToCelsius (self, fahrenheit):
        return (fahrenheit - 32) * (5/9)
 
# Second class.
from tkinter import *

class Second:
    def __init__ (self, root = None):
        super (view, self).__init__ (root)
        self.inputText = StringVar()
        self.outputText = StringVar()
        self.radioChoice = IntVar()
        
        # Creating labels.
        Label (self, text = 'Initial Temperature: ').grid (row = 0, column = 0)                    
        Entry (self, textvariable = self.inputText).grid (row = 0, column = 1, columnspan = 2, sticky = 'ew')
        Label (self, text = ': ').grid (row = 1, column = 0)
        Radiobutton (self, text = 'Celsius', variable = self.radioChoice, value = 1).grid (row = 1,column = 1)
        Radiobutton (self, text = 'Fahrenheit', variable = self.radioChoice, value = 2).grid (row = 1, column = 2)
        Label (self, text = 'Converted Temperature: ').grid (row = 2, column = 0)
        Label (self, textvariable = self.outputText).grid (row = 2, column = 1, columnspan = 2, sticky = 'ew')
        self.radioChoice.set(1)
 
    # Input temperature converted.
    def getInputTemperature (self):
        return float (self.inputText.get())
 
    # Updating output label.
    def setOutput (self, output):
        self.outputText.set (output)
 
    # Returns true if Celsius is selected as the current source temperature.
    def isCelsiusSelected (self):
        return self.radioChoice.get() == 1
 
# Third class.
import tkinter
 
class Third:
    def __init__ (self):
        self.first = first.First()
        root = tkinter.Tk()
        self.second = second.Second
        self.second.pack()
        b = tkinter.Button (root, text = 'Convert to Celsius/Fahrenheit', command = self.convert).pack()
        root.mainloop()
 
    # Converting between the two temperatures.
    def convert (self):
        try:
            # Input temperature.
            tempSource = self._view.getInputTemperature()
            # Identifying source temperature.
            if self._view.isCelsiusSelected():
                # Converting to Fahrenheit if Celsius is chosen.
                tempDest = self._model.convertToFahrenheit (tempSource)
                # Displaying output with temperature.
                self._view.setOutput ('{:.1f}F'.format (tempDest))
            else:
                # Converting to Celsius.
                tempDest = self._model.convertToCelsius (tempSource)
                self._view.setOutput ('{:.1f}C'.format (tempDest))
        except:
            # Displaying message if input is invalid.
            self._view.setOutput ("Invalid input. Please try again.")
 
# GUI initializing.
c = Third()