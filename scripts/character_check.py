'''
FileName: character_check.py
Author: John Delgado
Created Date: 8/5/2020
Version: 1.0 Initial Development

There are probably a couple different ways valiate a string for ascii characters
    * Regex
    * built in string method .isAscii()

created it's own function for unit testing functionality and in case requirements change later. 

    Pros of choosing Regex
        * Powerful
        * multiple conditions can be checked at once
    Cons of choosing Regex
        * can get confusing quickly
        * could decrease performance if regex has too many checks

    Pros of choosing built in is.Ascii()
        * easier for readability and maintainability
    Cons of choosing is.Ascii()
        * needs at least python version 3.7
        * if requirements change will have to re-write this entire function again
        * After writing that last Con, I feel if I choose this method I'm going to regret it later. 

'''
import re  # regular expression module


def check_password_characters(password,regEx, debug):
    if(debug):
        print()
        print("Entering Ascii Character check")
        print("password is: {}".format(password))

    
    regExpression = regEx
    check = re.match(regEx,password)

    if(debug):
        print("Regex is: {}".format(regEx))
        print("Regular Expression check is: {}".format(check))

    if(check):
        if(debug):
            print("Password String {} contains only ascii characters".format(password))
        return True

    else:
        print("Password: '{}' contains Unicode or illegal characters. Ascii check has failed validation".format(password))
        return False
