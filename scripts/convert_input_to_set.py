#!/usr/bin/python
'''
FileName: convert_input_to_set.py
Author: John Delgado
Created Date: 8/7/2020
Version: 1.0 Initial Development

This will take the sys.stdin input and convert it into a set and then return the set 
'''

def convert_input_to_set(inputVales,debug):
    if(not inputVales):
        raise Exception("Input is empty. Please provide values.")

    uniqueSet = set()
    for line in inputVales:
        if(debug):
            print("Adding value: {} to set ".format(line))

        uniqueSet.add(line)
        
    return uniqueSet
