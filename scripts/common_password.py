#!/usr/bin/python
'''
FileName: common_password.py
Author: John Delgado
Created Date: 8/5/2020
Version: 1.0 Initial Development

This function will be running the current string against a new line delimited list of common passwords and password pharases that are not allowed.

'''
import re


def common_password_check(password, exclude_list, print_valid, debug):
    if(debug):
        print("Entered common Password Check")
        print("Password is: {}".format(password))
        print("Exclude list is: {}".format(exclude_list))
        print("encoded password is: {}".format(password.encode()))

    valid_password_check = re.search(password.encode(),
                                    exclude_list)

    if(debug):
        print(valid_password_check)

    if(valid_password_check):
        print("Password: {} was found on the common password exception list.".format(password))
        return True

    else:
        if((debug) or (print_valid)):
            print("Password {} was a valid password. Moving to nextline.".format(password))

        return False
