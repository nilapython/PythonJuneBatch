'''
Created on Jul 20, 2019

@author: Nilambari
'''

class InvalidInputError(RuntimeError):

    def __init__(self, errorMessage):
        self.errorMessage = errorMessage
        