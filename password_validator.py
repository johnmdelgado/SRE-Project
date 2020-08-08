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
from scripts import length_validation
from scripts import character_check
from scripts import file_importer
from scripts import common_password
from scripts import convert_input_to_set
from inspect import currentframe, getframeinfo
import sys
import os

def password_validator(converted_set,file_path):
#    if(not filePath):
#         print("No file provided using default file from: {}".format(config["password_defaults"]["excludedPWFilepath"]))
#         filePath = config["password_defaults"]["excludedPWFilepath"]
    
    excluded_passwords = file_importer.file_importer(file_path,
        config["debugging"]["debug"])

    for line in converted_set:
        # First check if password meets the length requirement. Fastest check for performance
        # Parameters are set from config file, except the dynamic Line that is being read
        # If the string fails this check, it will move to the next line in the file

        formatted_string = line.rstrip() # Need to strip new line character


        length_check = length_validation.length_validation(config["password_defaults"]["min_pw_length"],
                                                          config["password_defaults"]["max_pw_length"],
                                                          formatted_string,  
                                                          config["debugging"]["debug"])  


        if(not length_check):
            continue 
        
        # included the ascii only check in case requirements change to allow unicode characters
        # However if requirements change to exclude different characters. 
        # This flag can be flipped to false and the regex in the function can be modified
        if(config["password_defaults"]["ascii_only"]):
            ascii_check = character_check.check_password_characters(formatted_string,
                                                                   config["password_defaults"]["password_regex"],
                                                                   config["debugging"]["debug"])  
            
            if(not ascii_check):
                continue 

        common_password_check = common_password.common_password_check(formatted_string,
                                                                     excluded_passwords,
                                                                     config["output_settings"]["output_valid_passwords"],
                                                                     config["debugging"]["debug"]) 
        if(common_password_check):
            continue

if __name__ == '__main__':
    # import config yaml file for Password requirements
    # requirements could change at a later date and easy to use same configs for test cases
    with open("./configs/config.yaml", "r") as ymlfile:
        config = yaml.safe_load(ymlfile)

    if(len(sys.argv) == 1):
        print("No file provided using default file from: {}".format(config["password_defaults"]["excluded_pw_filepath"]))
        file_path = config["password_defaults"]["excluded_pw_filepath"]
    else:
        file_path = sys.argv[1]

    converted_set = convert_input_to_set.convert_input_to_set(sys.stdin,
                                                             config["debugging"]["debug"])

    password_validator(converted_set,file_path)