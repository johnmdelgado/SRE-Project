#!/usr/bin/python
'''
FileName: commonPassword.py
Author: John Delgado
Created Date: 8/5/2020
Version: 1.0 Initial Development

This function will be running the current string against a new line delimited list of common passwords and password pharases that are not allowed. 

'''

def commonPasswordCheck(password,exludeList,debug):

    validPasswordCheck = exludeList.find(password)

    if(not validPasswordCheck):
        print("Password: {} was found on the common password exception list.".format(password))
        return False
    
    else:
        if(debug):
            print("Password {} was a valid password. Moving to nextline.".format(password))

        return True
