#Author: Ryan Young
#Date: 8/1/19
#Description: This program is my solution for MIT Open Course Ware, Problem Set 0. I wrote the code in order to re-establish a basic understanding of Python for myself.
#             The link to the problems are here: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/assignments/
#
#Problem Set
#Write a program that does the following in order:
#   1. Asks the user to enter a number “x”
#   2. Asks the user to enter a number “y”
#   3. Prints out number “x”, raised to the power “y”.
#   4. Prints out the log (base 2) of “x”.
#
#Editing History
#8/1/19    Version 1.00     Created the program

import math

varX = input("1. Please enter a number x: ")
varX = int(varX)
varY = input("2. Please enter a number y: ")
varY = int(varY)
print("User input for x was: ", varX)
print("User input for y was: ", varY)
output = varX**varY
print("3. x raised to the power of y is: ", output)
output = math.log(varX,2)
print("4. Log (base 2) of x is: ", output)

