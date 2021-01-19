"""
Student: Griffin Gowdey.
Instructor: Dorothy Harman.
Class Number: ITSE1479-20234
Class Name: Intro to Scripting Languages.
Semester: Fall 2020.
Part 1.

Assignment:
A local biologist needs a program to predict population growth. 
The inputs would be the initial number of organisms, the rate of 
growth (a real number greater than 0), the number of hours it takes 
to achieve this rate, and a number of hours during which the population 
grows. 

For example, one might start with a population of 500 organisms, a 
growth rate of 2, and a growth period to achieve this rate of 6 hours.  
Assuming that none of the organisms die, this would imply that this 
population would double every 6 hours.  Thus, after allowing 6 hours 
for growth, we would have 1000 organisms, and after 12 hours, we would 
have 2000 organisms.  Write a program that takes the inputs from the 
viewer and displays a prediction of the total population.

Pseudocode:
Input: Int for number of organisms, hours to achieve rate, and hours
during population growth. Float for rate of growth.
Process: For loop and equation to predict population growth.
Output: Print line for population growth.
"""

# User inputs the initial number of organisms.
NumberOfOrganisms =  int (input ("Enter the initial number of organisms: "))

# User inputs the rate of growth (a real number greater than 0).
RateOfGrowth = float (input ("Enter the rate of growth [a real number greater than 0]: "))

# User inputs the number of hours it takes to achieve this rate.
HoursToAchieveRate = int (input ("Enter the number of hours to achieve the rate of growth: "))

# User inputs the number of hours during which the population grows.
HoursDuringPopulationGrowth = int (input ("Enter the total hours of growth: "))

# PopulationGrowth/NumberofOrganisms count for loop.
PopulationGrowth = NumberofOrganisms = 0

# Hours count for loop.
Hours = 1

# Loop/equation to solve problem.
while Hours < HoursDuringPopulationGrowth:
    PopulationGrowth *= RateOfGrowth
    Hours += HoursDuringPopulationGrowth
    print (Hours)

if Hours <= HoursDuringPopulationGrowth:

# Display message with population growth.
    print("The total population growth is: " + PopulationGrowth)