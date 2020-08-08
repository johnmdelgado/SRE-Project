#!/usr/bin/python
'''
FileName: __test__length_validation.py
Author: John Delgado
Created Date: 8/7/2020
Version: 1.0 Initial Development

This is the testing file for the length_validation.py
'''

import random
import string
import yaml
import unittest
import length_validation
import os
import sys
import inspect
functions_dir = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))) + "/scripts"  # scripts Directory
print(functions_dir)
sys.path.insert(0, functions_dir)

with open("../configs/config.yaml", "r") as ymlfile:
    config = yaml.safe_load(ymlfile)


class passwords_test_case(unittest.TestCase):

    # ========================================================================================
    # False test cases
    # ========================================================================================
    def test_empty_string(self):
       # empty String
       test_string = ""
       result = length_validation.length_validation(config["password_defaults"]["min_pw_length"],
                                                   config["password_defaults"]["max_pw_length"],
                                                   test_string,
                                                   config["debugging"]["test_debug"])
       self.assertFalse(result)

    def test_spaceAsString(self):
       # Space character String
       test_string = " "
       result = length_validation.length_validation(config["password_defaults"]["min_pw_length"],
                                                   config["password_defaults"]["max_pw_length"],
                                                   test_string,
                                                   config["debugging"]["test_debug"])
       self.assertFalse(result)

    def test_stringMinLengthMinusOne(self):
       # String Length of one less than the minimum allowed from constant

       # Generate a random string with a length of -1 of the minumum threshold
       n = config["password_defaults"]["min_pw_length"] - 1
       test_string = ''.join(random.choices(
           string.ascii_uppercase + string.digits, k=n))

       result = length_validation.length_validation(config["password_defaults"]["min_pw_length"],
                                                   config["password_defaults"]["max_pw_length"],
                                                   test_string,
                                                   config["debugging"]["test_debug"])
       self.assertFalse(result)

    def test_stringMaxLengthPlusOne(self):
       # String Length of one more than the maximum allowed from constant

       # Generate a random string with a length of +1 of the minumum threshold
       n = config["password_defaults"]["max_pw_length"] + 1
       test_string = ''.join(random.choices(
           string.ascii_uppercase + string.digits, k=n))

       result = length_validation.length_validation(config["password_defaults"]["min_pw_length"],
                                                   config["password_defaults"]["max_pw_length"],
                                                   test_string,
                                                   config["debugging"]["test_debug"])
       self.assertFalse(result)

    # ========================================================================================
    # True test cases
    # ========================================================================================

    def test_stringMinLength(self):
       # String Length of the minimum allowed from constant

       # Generate a random string with a length of the minumum threshold
       n = config["password_defaults"]["min_pw_length"]
       test_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k = n)) 

       result = length_validation.length_validation(config["password_defaults"]["min_pw_length"],
                                                   config["password_defaults"]["max_pw_length"],
                                                   test_string,
                                                   config["debugging"]["test_debug"])
       self.assertTrue(result)

    def test_stringMinLengthPlusOne(self):
       # String Length of one Plus than the minimum allowed from constant

       # Generate a random string with a length of +1 of the minumum threshold
       n = config["password_defaults"]["min_pw_length"] + 1
       test_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k = n)) 

       result = length_validation.length_validation(config["password_defaults"]["min_pw_length"],
                                                   config["password_defaults"]["max_pw_length"],
                                                   test_string,
                                                   config["debugging"]["test_debug"])
       self.assertTrue(result)

    def test_stringMaxLengthMinusOne(self):
       # String Length of one less than the maximum allowed from constant

       # Generate a random string with a length of -1 of the maximum threshold
       n = config["password_defaults"]["max_pw_length"] - 1
       test_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k = n)) 

       result = length_validation.length_validation(config["password_defaults"]["min_pw_length"],
                                                   config["password_defaults"]["max_pw_length"],
                                                   test_string,
                                                   config["debugging"]["test_debug"])
       self.assertTrue(result)

    def test_stringMaxLength(self):
       # String Length of the maximum allowed from constant

       # Generate a random string with a length of the maximum threshold
       n = config["password_defaults"]["max_pw_length"]
       test_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k = n)) 

       result = length_validation.length_validation(config["password_defaults"]["min_pw_length"],
                                                   config["password_defaults"]["max_pw_length"],
                                                   test_string,
                                                   config["debugging"]["test_debug"])
       self.assertTrue(result)
    

if __name__ == '__main__':
    unittest.main()
