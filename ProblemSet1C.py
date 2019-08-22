#Author:
#Date: 8/15/19
#Location: MIT Open Course Ware, Introduction to Computer Science and Programming in Python (MIT 6.0001)
#Description: A basic bidirectional search algorithm. Does searches faster than a linear search.
#               Requires the array to be ordered smallest to largest
#Editing History
#8/15/19    Version 1.00     Created the bidirectional search portion of the program
#8/22/19    Version 1.01     Created the check accuracy function and began to attach it to the bidirectional search
#8/23/19    Version 1.02     Solved a logic error in the while-not loop

from __future__ import division
import array as arr

#Given values from the problem set
semi_annual_raise = .07
r = .04
downpayment = 250000

#Take User input and calculate secondary variables
annual_salary = input("Enter your annual salary: ")
annual_salary = float(annual_salary)
monthly_salary = annual_salary/12
portion_saved = 1
monthSavings = portion_saved * monthly_salary

#######################################################################################################################
# Function: checkAccuracy()
# Incoming: the amount the user saves on a monthly basis
# Return: 1 if the value is found, 0 if the value has not been found
# Description: given a monthly saved amount, calculates if it's possible to hit a savings of $250,000 +/- $100 after
#               36 months
#######################################################################################################################
def checkAccuracy(monthly_saved = 1):
    # On the first month we get paid at the end of the month but do not receive interest from it.
    current_savings = 0
    month = 1
    current_savings = current_savings + monthly_saved
    #print("At the end of month ", month, "you have: $", monthly_saved,)
    month = month + 1

    #From then on we get intereste and then increment the month
    while (month != 37):
        interest = current_savings*r/12
        current_savings = current_savings + monthly_saved + interest
        #print("At the end of month ", month, "you have: $", current_savings, ", Of this $", interest, " was from interest.")
        checkRaise = month % 6
        if (checkRaise == 0):
            monthly_saved = monthly_saved * (1 + semi_annual_raise)
            #print("YOU EARNED A RAISE! Your new monthly salary is, ", monthly_saved)
        month = month + 1

    #The while loop did not need to add an addtional month at the end of the loop. For coding reasons this couldn't be stopped.
    month = month - 1
    #print("With a monthly savings of", monthly_saved, "you saved ", current_savings)
    return current_savings

#Start by creating an array of floats 0.0 - 100.0 representing percentages.
count = 0
percentages = arr.array('d', [])
while (count != 10001):
    percentages.append(count/100)
    #print ("The number", percentages[count], "has been placed into the array at location", count)
    count = count + 1
print("Array has been created")

#search for a target number in the array with bisection search
highIndex = len(percentages)        #The highest index in the array you will search. Starts at 10,000
lowIndex = 0                        #The lowest index in the array you will search. Starts at 0
searchAt = 0                        #The box you want to search
discoveredValue = 0                 #The value that the box you searched contains
steps = 0                           #How many steps the bidirectional search algorythm has done. Tracks efficeiency.
amount_saved = 0                    #The total amount saved given a salary and a percentage savings rate
fail = 0                            #Triggers if it's impossible to save enough with a too small salary

#First check if it's possible to save enough if you save 100% of your monthly salary
if (checkAccuracy(monthly_salary) < downpayment):
    print ("It's not possible to save enough for your down payment with your current salary")
    amount_saved = 250000
    fail = 1

while not ((downpayment-100) <= amount_saved <= (downpayment+100)):
    searchAt = int((highIndex + lowIndex) / 2)      #search in the middle of the highest and lowest index
    discoveredValue = percentages[searchAt]         #grab the value at that middle index
    print("The loop tests value ", discoveredValue, "at step ", steps)
    #Get the value of the monthly salary * the percentage savings rate
    amount_saved = checkAccuracy(monthly_salary*(discoveredValue/100))
    if(steps > 100):
        print("ERROR: The program could not find the target within +/- $100. This is likely because the starting salary"
              " is too high.")
        amount_saved = 250000
    elif(amount_saved < downpayment):                #if the discovered value is smaller than the target
        lowIndex = searchAt                         #remove this entry and all lower entries from the search area
        print("Target not found, the loop will now search in boxes between,", highIndex, "and", lowIndex)
    elif(amount_saved > downpayment):              #if the discovered value is larger than the target
        highIndex = searchAt                        #remove this entry and all higher entries from the search area
        print("Target not found, the loop will now search in boxes between,", highIndex, "and", lowIndex)
    else:
        print("The target has been found! Location ", searchAt, "contains value ", discoveredValue)
    steps = steps + 1

if (fail != 1):
    print("Best savings rate: ", discoveredValue)
    print("Steps in bisection search: ", steps)
    print("Amount saved: ", amount_saved)