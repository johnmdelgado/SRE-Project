#!/usr/bin/python
'''
FileName: length_validation.py
Author: John Delgado
Created Date: 8/7/2020
Version: 1.0 Initial Development

This will take password length thresholds from a config file and compare the password against those constraints.
Returns true or false boolean
'''
# Eliminating use cases so that our regex won't have to account for length as well.
def length_validation(min_length, max_length, password,debug):
    #Debugging code
    if(debug):
        print()
        print("Entering Length check")
        print("minlength is: {} ".format(min_length))
        print("maxlength is: {}".format(max_length))
        print("password is: {}".format(password))
        print("Length of password is: {}".format(len(password)))

    #check if string is null or empty
    if((len(password) == 0) or (not password)):
        print("Password is null or empty. Please use a password between {} and {} characters:".format(min_length, max_length))
        return False

    if(len(password) < min_length):
        print("Password: {} is too short. Does not meet length requirement of: {}".format(password,min_length))
        return False

    if(len(password) > max_length):
        print("Password: {} is too Long. Exceeds length requirement of: {}".format(password,max_length))
        return False
        
    else:
        if(debug):
            print("Password: {} is a valid length".format(password))

        return True
