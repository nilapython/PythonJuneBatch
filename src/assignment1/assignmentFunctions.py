'''
Created on Jul 21, 2019

@author: Nilambari
'''
from assignment1.InvalidInputError import InvalidInputError
import random
def checkInput(varStr,iType):
    try:
        x = int(varStr)
        if (iType == "S" or (iType == "N" and (x < 1 or x > 100))):
            raise InvalidInputError("Invalid input ...")
        return x
    except ValueError:
        if (iType == "N"):
            raise InvalidInputError("Invalid input ...")
        elif (iType == "S"):
            return varStr

def getInput(inputType):   
    while True:
        try:
            #print("\n")
            varName = input()
            if len(varName.strip()) > 0:
                return checkInput(varName,inputType)
                break
            else:
                print("Enter input")
                continue
        except InvalidInputError as error:
            print(error,"Try again")
            continue
        else:
            continue
 
def printMessage(vMsg,iCount):
    for i in range(iCount):
        print(vMsg)

def numberEvenOdd(iNum,iDivide):
    if iNum%iDivide == 0:
        return 'Number '+str(iNum)+' is divisible by '+str(iDivide)+' OR an Even number.'
    else:
        return 'Number '+str(iNum)+' is NOT divisible by '+str(iDivide)+' OR an Odd number.'
    
def compareNumlist(iCompare,iList):
    newList = []
    for eachNum in iList:
        if eachNum < iCompare:
            newList.append(eachNum) 
            
    return newList

def numberCommonLists(iList1, iList2):
    newList = []
    if len(iList1) > len(iList2):
        tempList = iList1
        iList1 = iList2
        iList2 = tempList
    for eachNum1 in iList1:
        for eachNum2 in iList2:
            if (eachNum1 == eachNum2 and eachNum1 not in newList):
                newList.append(eachNum2)
    return newList

def generateRandomNumberList(startNum,iCount,iRange,iDuplicate):
    randomList =[]
    #for x in range(iCount):
    x = 1
    while x <= iCount:
        y = random.randint(startNum,iRange)
        if (iDuplicate == "N" and y not in randomList) or (iDuplicate != "N"):
            randomList.append(y)
            x = x + 1
        else:
            continue
        
    return randomList

def divisorList(iNumber):
    newList = []
    for x in range(1,iNumber+1):
        if iNumber%x == 0:
            newList.append(x)
    return newList
    
                             
                             