"""
Student: Griffin Gowdey.
Instructor: Dorothy Harman.
Class Number: ITSE1479-20234
Class Name: Intro to Scripting Languages.
Semester: Fall 2020.
Part 1.

Assignment:
See "Turtle Shapes To Program" PDF file in Lab 5 folder for original 
questions and example graphics.

1.) Draw a square.
2.) Draw a 5-pointed star.
3.) Draw an example of changing line color.
If you want to use other colors: 
https://www.webfx.com/web-design/color-picker/. 
Specify the colors with a # and the hexadecimal code. 
There are many color pickers on the web for use, this is just one.
4.) Draw a hexagon shape.
5.) Draw a grid of dots. 5 dots wide and 7 dots high.
6.) Draw any one of the spiral shapes (see PDF in the Lab 5 folder) 
or create your own spiral shape.
"""

# Turtle import for all questions/subsections.
import turtle

# 1.) Draw a square.
turtle.forward (50)
turtle.left (90)
turtle.forward (50)
turtle.left (90)
turtle.forward (50)
turtle.left (90)
turtle.forward (50)
turtle.left (90)

turtle.exitonclick()

# 2.) Draw a 5-pointed star.
for x in range (5):
    turtle.forward (400)
    turtle.right (144)
    turtle.done

turtle.exitonclick()

# 3.) Draw an example of changing line color.
colors = ["red", "blue", "green", "gray", "orange", "black"]

for x in range (100):
  turtle.forward (5 + x)
  turtle.right (15)
  turtle.color (colors[x%6])
  turtle.done

# 4.) Draw a Hexagon Shape.
for x in range (6):
    turtle.forward (100)
    turtle.right (60)

turtle.exitonclick()

# 5.) Draw a grid of dots. 5 dots wide and 7 dots high.
grid = turtle.turtle()
dot_distance = 10
width = 5
height = 7
grid.penup ()
grid.setposition (100, 0)

for y in range (height):
    for x in range (width):
      grid.dot ()
      grid.forward (dot_distance)

grid.backward (dot_distance * width)
grid.right (90)
grid.forward (dot_distance)
grid.left (90)

turtle.exitonclick()

# 6.) Draw any one of the spiral shapes or create your own spiral shape.
for x in range (100):
  turtle.forward (5 + x)
  turtle.right (15)
  turtle.done