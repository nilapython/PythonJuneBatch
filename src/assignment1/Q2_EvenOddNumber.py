'''
Created on Jul 21, 2019

@author: Nilambari
'''

from assignment1.assignmentFunctions import checkInput, getInput, numberEvenOdd

print("Number to Check ...")
varCheck = getInput("N")
#print("Number to check is ",varCheck)

print("Number to divide by ...")
varDivide = getInput("N")
#print("Number to divide by ",varDivide)
print(numberEvenOdd(varCheck,varDivide))

