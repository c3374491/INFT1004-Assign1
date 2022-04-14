#
# Author: c3374491 (Ethan Davey)
# Date: 02/03/21
# Functionality: Finding the circumference, area and radius of defined circles.
# To Do: All tasks have been completed.
#

import math # Importing math allows the use of pi and square root.
pi = math.pi # Assigning math.pi to pi to be used within functions.


def circumference(radius):
    # The math formula to find circumference from radius performed and returned 
    return (2 * pi * radius)
    
def area(radius):
    # The math formula to find area from radius performed and returned 
    return (pi * radius ** 2)
    
def radiusFromCircumference(circumference):
    # The math formula to find radius from circumference performed and returned 
    return (circumference / (pi * 2))
    
def radiusFromArea(area):
    # The math formula to find radius from area performed and returned 
    return (math.sqrt((area / pi)))
    

def circles_of_radius(low, high):
    # The loop to excecute and display the outcomes for the first value up to the final value minus one
    for i in range(low, high):
        print("A circle with radius of", i, "has circumference", circumference(i), "and area", area(i))

def circles_of_circumference(low, high):
    # The loop to excecute and display the outcomes for the first value up to the final value minus one
    for i in range(low, high):
        print("A circle with a circumference of", i, "has radius", radiusFromCircumference(i), "and area", area(radiusFromCircumference(i)))

def circles_of_area(low, high):
    # The loop to excecute and display the outcomes for the first value up to the final value minus one
    for i in range(low, high):
        print("A circle with an area of", i, "has radius", radiusFromArea(i), "and circumference", circumference(radiusFromArea(i)))