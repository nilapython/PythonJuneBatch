'''
Created on Jul 21, 2019

@author: Nilambari
'''
from assignment1.assignmentFunctions import checkInput, getInput, divisorList

print("Enter Number to Check ...")
varCheck = getInput("N")

print("Divisors for number",varCheck,"are",divisorList(varCheck))