'''
Created on Jul 20, 2019

@author: Nilambari
'''
#from assignment1.InvalidInputError import InvalidInputError
import datetime
from assignment1.assignmentFunctions import getInput, printMessage

print('Enter Name :: ') 
varName = getInput("S")
#print("Name is ",varName) 
 
print('Enter Age :: ') 
varAge = getInput("N")
#print("Age is ",varAge)   

print('Print message how many times? ') 
varCount = getInput("N")
#print("varCount is ",varCount) 

now = datetime.datetime.now()
#print(now.year)
varYear=int(now.year)

msg = varName+" will turn 100 years in Year "+str(varYear+(100-varAge))
#print(msg)
printMessage(msg,varCount)

   


