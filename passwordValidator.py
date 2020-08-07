#!/usr/bin/python
'''
FileName: PasswordValidator.py
Author: John Delgado
Created Date: 8/5/2020
Version: 1.0 Initial Development

This program will be checking a list of passwords from a file and validating each line in that file that it meets the all the requirements below. 
If any of the requirements are not met the program will output to the console the password that did not pass the validation and the reason it
did not pass.

================================= NIST Guidelines ====================================================================
* Have an 8 character minimum
* AT LEAST 64 character maximum
* Allow all ASCII characters and spaces (unicode optional)
* Not be a common password

================================= Project Guidelines ====================================================================

* Use a 64 character maximum and allow only ASCII characters.
* As for checking if the password is common, the program should take a file of newline delimited common passwords and efficiently check if a password is in that file.
* Of course leverage appropriate data structures, but try to be efficient in your resource usage. 
* Use this Common Password List to develop with, but the program should be able to be supplied with any newline delimited file. 
* The program should accept passwords from STDIN in newline delimited format and print invalid passwords to the command line. 

An example usage would look like the following: (asterixes used to print unprintable chars)

cat input_passwords.txt | ./password_validator weak_password_list.txt
mom -> Error: Too Short
password1 -> Error: Too Common
***  Error: Invalid Charaters
'''

# Modules to import
import unittest
import yaml
import fileinput
from Functions import length
from Functions import outputFailure
from Functions import characterCheck
from Functions import fileImporter
from inspect import currentframe, getframeinfo
import sys

def passwordValidator(filePath):
    if(not filePath):
        print("No file provided using default file from: {}".format(config["passwordDefaults"]["excludedPWFilepath"]))
        filePath = config["passwordDefaults"]["excludedPWFilepath"]
    
    dataSet = fileImporter(filePath,
        config["debugging"]["debug"])
    print(dataSet)

    # import config yaml file for Password requirements
    # requirements could change at a later date and easy to use same configs for test cases
    with open("./configs/config.yaml", "r") as ymlfile:
        config = yaml.safe_load(ymlfile)

    # if testing is enabled. Generate unit testing results
    if(config["testing"]["testAtRun"]):
        unittest.main()


    # TODO maybe need to add batching or parrellism. Huge files could be a problem.

    for line in sys.stdin:
        # First check if password meets the length requirement. Fastest check for performance
        # Parameters are set from config file, except the dynamic Line that is being read
        # If the string fails this check, it will move to the next line in the file

        formattedString = line.rstrip() # Need to strip new line character


        lengthCheck = length.passwordLengthCheck(
            config["passwordDefaults"]["minPWLength"],
            config["passwordDefaults"]["maxPWLength"],
            formattedString,  
            config["debugging"]["debug"])  


        if(not lengthCheck):
            # TODO get current line number. Could cause performance issue for large files
            failedValidation = "length"

            outputFailure.outputFailure(failedValidation,
                config["debugging"]["debug"])
            continue # length check end
        
        # included the ascii only check in case requirements change to allow unicode characters
        # However if requirements change to exclude different characters. 
        # This flag can be flipped to false and the regex in the function can be modified
        if(config["passwordDefaults"]["asciiOnly"]):
            asciiCheck = characterCheck.checkPasswordCharacters(
                formattedString,
                config["passwordDefaults"]["passwordRegEx"],  
                config["debugging"]["debug"])  
            
            if(not asciiCheck):
                failedValidation = "illegal character"

                outputFailure.outputFailure(failedValidation,
                    config["debugging"]["debug"])
                continue # illegal character check end
        

