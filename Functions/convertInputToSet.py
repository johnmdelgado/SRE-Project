#!/usr/bin/python
'''
FileName: commonPassword.py
Author: John Delgado
Created Date: 8/7/2020
Version: 1.0 Initial Development

This will take the sys.stdin input and convert it into a set and then return the set 
'''

def convertInputToSet(inputVales,debug):
    if(not inputVales):
        raise Exception("Input is empty. Please provide values.")

    uniqueSet = set()
    for line in inputVales:
        if(debug):
            print("Adding value: {} to set ".format(line))

        uniqueSet.add(line)
        
    return uniqueSet
