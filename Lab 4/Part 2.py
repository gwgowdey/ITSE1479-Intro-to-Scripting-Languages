"""
Student: Griffin Gowdey.
Instructor: Dorothy Harman.
Class Number: ITSE1479-20234
Class Name: Intro to Scripting Languages.
Semester: Fall 2020.
Part 2.

Assignment:
Use the "Turtle" python feature to draw a square.
"""

# Importing "Turtle" python feature.
import turtle

# Importing an actual turtle for the shape instead of a triangle.
turtle.shape ("turtle")

# Drawing a square with the turtle as our icon.
turtle.forward (50)
turtle.left (90)
turtle.forward (50)
turtle.left (90)
turtle.forward (50)
turtle.left (90)
turtle.forward (50)
turtle.left (90)

# Keeps the drawing window open until user clicks on it.
turtle.exitonclick ()