'''
Created on Jul 21, 2019

@author: Nilambari
'''
from assignment1.assignmentFunctions import getInput, generateRandomNumberList, numberCommonLists

print("How many numbers to generate for List 1 ? ")
varCount1 = getInput("N")

print("How many numbers to generate for List 2 ? ")
varCount2 = getInput("N")

print("Enter high value of number range ... ")
varRange = getInput("N")

varList1 = generateRandomNumberList(1,varCount1,varRange,"N")
print("List 1 is ",varList1)

varList2 = generateRandomNumberList(1,varCount2,varRange,"N")
print("List 2 is ",varList2)

print(numberCommonLists(varList1,varList2))

