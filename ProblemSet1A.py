#Author: Ryan Young
#Date: 8/1/19
#Location: MIT Open Course Ware, Introduction to Computer Science and Programming in Python (MIT 6.0001)
#Description: House Hunting. Takes a user's annual salary, savings rate and cost of a dream home to determine
#             how many months it will take them to save for it. It assumes a 25% down payment and a 4% monthly interest rate
#
#Editing History
#8/1/19    Version 1.00     Created the program

portion_down_payment = .25
current_savings = 0
r = .04
month = 0

#Take user input
annual_salary = input("Enter your annual salary: ")
annual_salary = float(annual_salary)
portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
portion_saved = float(portion_saved)
total_cost = input("Enter the cost of your dream home: ")
total_cost = float(total_cost)

#Check user input
print("")
print("Annual Salary: ", annual_salary)
print("Portion Saved for down payment: ", portion_saved)
print("Total Cost of your home: ", total_cost)
print("")

#Calculate secondary variables from the initial user input
downpayment = portion_down_payment * total_cost
monthly_salary = annual_salary/12
monthly_saved = portion_saved*monthly_salary
print("With a cost of", total_cost, " the total amount needed for a 25% down payment is: ", downpayment)
print("By saving ", portion_saved, "of an monthly salary of ", monthly_salary, "you will save ", monthly_saved, " per month.")
print("")

#On the first month we get paid at the end of the month but do not receive interest from it.
month = 1
interest = 0
current_savings = current_savings + monthly_saved
print("At the end of month ", month, "you have: $", monthly_saved,)
month = month + 1

#From then on we
while (downpayment > current_savings):
    interest = current_savings*r/12
    current_savings = current_savings + monthly_saved + interest
    print("At the end of month ", month, "you have: $", current_savings, ", Of this $", interest, " was from interest.")
    month = month + 1

#The while loop did not need to add an addtional month at the end of the loop. For coding reasons this couldn't be stopped.
month = month - 1
print("Congratulations you have enough for your dream home.")
print("Number of months: ", month)