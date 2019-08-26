'''
Created on Jul 21, 2019

@author: Nilambari
'''

from assignment1.assignmentFunctions import getInput, compareNumlist, generateRandomNumberList

#varList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print("How many numbers to generate? ")
varCount = getInput("N")

print("Enter high value of number range ... ")
varRange = getInput("N")

print("Number to compare to ...")
varCompare = getInput("N")

varList = generateRandomNumberList(1,varCount,varRange,"Y")
print(varList)
print(compareNumlist(varCompare,varList))

