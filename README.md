# INFT1004-Assing1
INFT1004 - Assignment 1 [Python]

## YOUR ASSESSMENT TASK
For this assignment you are to write a Python program that works out various properties of a circle. 
Further details of the task are provided below.

## ASSIGNMENT TASK
You are required to write three functions, as explained below. The functions will be called `circles_of_radius()`, `circles_of_circumference()`, and `circles_of_area()`. Be sure to spell the function names exactly the same way that they are spelt here; otherwise, when we try to test them, the functions we are trying to test will not be found.<br>
A circle whose radius is r has a circumference of 2πr and an area of πr^2. In case you don’t know enough mathematics to read those formulas, π is the value discussed in section 3.2 of Downey as math.pi; symbols run together are to be multiplied, so 2πr means 2 × π × r; and a superscript of 2 means that the preceding symbol is squared, or multiplied by itself, so πr^2 means π × r × r.<br>
Those formulas tell you how to get the circumference and the area if you know the radius. From them, you can work out formulas to tell you how to get the radius if you know the circumference, and how to get the radius if you know the area.<br>
All three of the functions will take two arguments, a lower integer and a higher integer.<br>
`circles_of_radius(low, high)` will calculate the circumferences and areas of circles with radiuses ranging from low to just short of high, and display them in a particular way;<br>
`circles_of_circumference(low, high)` will calculate the radiuses and areas of circles with circumferences ranging from low to just short of high, and display them in a particular way;<br>
`circles_of_area(low, high)` will calculate the radiuses and circumferences of circles with areas ranging from low to just short of high, and display them in a particular way.<br>
Here are examples of the output that should be produced by each function:

```
>>>circles_of_radius(3, 7)
A circle with radius 3 has circumference 18.84955592153876 and area 28.274333882308138
A circle with radius 4 has circumference 25.132741228718345 and area 50.26548245743669
A circle with radius 5 has circumference 31.41592653589793 and area 78.53981633974483
A circle with radius 6 has circumference 37.69911184307752 and area 113.09733552923255

>>> circles_of_circumference(22,25)
A circle with circumference 22 has radius 3.5014087480216975 and area 38.515496228238675
A circle with circumference 23 has radius 3.660563691113593 and area 42.096482447806316
A circle with circumference 24 has radius 3.819718634205488 and area 45.83662361046586

>>> circles_of_area(9, 13)
A circle with area 9 has radius 1.692568750643269 and circumference 10.634723105433096
A circle with area 10 has radius 1.7841241161527712 and circumference 11.209982432795858
A circle with area 11 has radius 1.8712051592547776 and circumference 11.757128763348256
A circle with area 12 has radius 1.9544100476116797 and circumference 12.279920495357862
```

Your functions do not need to check that their arguments are suitable numbers. It will be the user’s responsibility to ensure this, and the functions can just assume it.<br>
Your program – the .py file that you hand in – will consist just of definitions for those three functions, along with appropriate comments and any import statements that you might need. It will not include calls to the functions: we will call the functions from the terminal when testing your programs.<br>
You should be sure to work through the week 2 lecture again, and chapters 3 and 4 of Downey, and to do the corresponding exercises, before starting work on these functions.<br>
When testing your functions, it would be wise to run them with exactly the arguments shown above, to check that they produce exactly the output shown above, except perhaps for very minor variations in the numbers.

## ASSESSMENT CRITERIA
Your work will be assessed as follows:
appropriate comments (1 mark)
- informative variable names (1 mark)
- correct function definition lines (1 mark)
- correct calculation of circumference from radius (1 mark)
- correct calculation of area from radius (1 mark)
- correct calculation of radius from circumference (1 mark)
- correct calculation of radius from area (1 mark)
- correct output, just as in the examples (3 marks)
Once these marks have been allocated, marks will be deducted for the following:
- failure to follow instructions/requirements, eg with file name
- syntax errors or runtime errors in your program (but we do not expect your function to deal with runtime errors caused by invalid function calls or arguments)
- late submission – see below<br>
While we encourage students to work together on the weekly exercises, this assignment is an individual assessment item, and each student is required to complete it without assistance from other students or other people. If the marker uncovers evidence that you have cheated in any way, for example, by sharing your code with others in the class, or by getting help from others, the matter will be reported to the Student Academic Conduct Officer as a potential case of academic misconduct.
