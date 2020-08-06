#!/usr/bin/python
# Eliminating use cases so that our regex won't have to account for length as well.
def passwordLengthCheck(minLength, maxLength, password,debug):
    #Debugging code
    if(debug):
        print()
        print("Entering Length check")
        print("minlength is: {} ".format(minLength))
        print("maxlength is: {}".format(maxLength))
        print("password is: {}".format(password))
        print("Length of password is: {}".format(len(password)))

    #check if string is null or empty
    if((len(password) == 0) or (not password)):
        print("Password is null or empty. Please use a password between {} and {} characters:".format(minLength,maxLength))
        return False
    if(len(password) < minLength):
        print("Password: {} is too short. Does not meet length requirement of: {}".format(password,minLength))
        return False
    if(len(password) > maxLength):
        print("Password: {} is too Long. Exceeds length requirement of: {}".format(password,maxLength))
        return False
    else:
        if(debug == True):
            print("Password: {} is a valid length".format(password))

        return True
