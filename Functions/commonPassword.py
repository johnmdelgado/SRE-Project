#!/usr/bin/python
'''
FileName: commonPassword.py
Author: John Delgado
Created Date: 8/5/2020
Version: 1.0 Initial Development

This function will be running the current string against a new line delimited list of common passwords and password pharases that are not allowed. 

'''
import re

def commonPasswordCheck(password,exludeList,debug):
    if(debug):
        print("Entered common Password Check")
        print("Password is: {}".format(password))
        print("Exclude list is: {}".format(exludeList.size()))
        print("encoded password is: {}".format(password.encode()))

    validPasswordCheck = re.search(password.encode(), exludeList)
    print(validPasswordCheck)

    if(validPasswordCheck):
        print("Password: {} was found on the common password exception list.".format(password))
        return False
    
    else:
        if(debug):
            print("Password {} was a valid password. Moving to nextline.".format(password))

        return True
