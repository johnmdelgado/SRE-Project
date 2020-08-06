#!/usr/bin/python

import random
import string
import yaml
import unittest
import length
import os
import sys
import inspect
functionsDir = os.path.dirname(os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))) + "/Functions"  # functions Directory
print(functionsDir)
sys.path.insert(0, functionsDir)

with open("../configs/config.yaml", "r") as ymlfile:
    config = yaml.safe_load(ymlfile)


class PasswordsTestCase(unittest.TestCase):

    # ========================================================================================
    # False test cases
    # ========================================================================================
    def test_emptyString(self):
       # empty String
       testString = ""
       result = length.passwordLengthCheck(config["passwordDefaults"]["minPWLength"],
        config["passwordDefaults"]["maxPWLength"],
        testString,
        config["debugging"]["testDebug"])
       self.assertFalse(result)

    def test_spaceAsString(self):
       # Space character String
       testString = " "
       result = length.passwordLengthCheck(config["passwordDefaults"]["minPWLength"],
        config["passwordDefaults"]["maxPWLength"],
        testString,
        config["debugging"]["testDebug"])
       self.assertFalse(result)

    def test_stringMinLengthMinusOne(self):
       # String Length of one less than the minimum allowed from constant

       # Generate a random string with a length of -1 of the minumum threshold
       n = config["passwordDefaults"]["minPWLength"] - 1
       testString = ''.join(random.choices(
           string.ascii_uppercase + string.digits, k=n))

       result = length.passwordLengthCheck(config["passwordDefaults"]["minPWLength"],
        config["passwordDefaults"]["maxPWLength"],
        testString,
        config["debugging"]["testDebug"])
       self.assertFalse(result)

    def test_stringMaxLengthPlusOne(self):
       # String Length of one more than the maximum allowed from constant

       # Generate a random string with a length of +1 of the minumum threshold
       n = config["passwordDefaults"]["maxPWLength"] + 1
       testString = ''.join(random.choices(
           string.ascii_uppercase + string.digits, k=n))

       result = length.passwordLengthCheck(config["passwordDefaults"]["minPWLength"],
        config["passwordDefaults"]["maxPWLength"],
        testString,
        config["debugging"]["testDebug"])
       self.assertFalse(result)

    # ========================================================================================
    # True test cases
    # ========================================================================================

    def test_stringMinLength(self):
       # String Length of the minimum allowed from constant

       # Generate a random string with a length of the minumum threshold
       n = config["passwordDefaults"]["minPWLength"]
       testString = ''.join(random.choices(string.ascii_uppercase + string.digits, k = n)) 

       result = length.passwordLengthCheck(config["passwordDefaults"]["minPWLength"],
        config["passwordDefaults"]["maxPWLength"],
        testString ,
        config["debugging"]["testDebug"])
       self.assertTrue(result)

    def test_stringMinLengthPlusOne(self):
       # String Length of one Plus than the minimum allowed from constant

       # Generate a random string with a length of +1 of the minumum threshold
       n = config["passwordDefaults"]["minPWLength"] + 1
       testString = ''.join(random.choices(string.ascii_uppercase + string.digits, k = n)) 

       result = length.passwordLengthCheck(config["passwordDefaults"]["minPWLength"],
        config["passwordDefaults"]["maxPWLength"],
        testString ,
        config["debugging"]["testDebug"])
       self.assertTrue(result)

    def test_stringMaxLengthMinusOne(self):
       # String Length of one less than the maximum allowed from constant

       # Generate a random string with a length of -1 of the maximum threshold
       n = config["passwordDefaults"]["maxPWLength"] - 1
       testString = ''.join(random.choices(string.ascii_uppercase + string.digits, k = n)) 

       result = length.passwordLengthCheck(config["passwordDefaults"]["minPWLength"],
        config["passwordDefaults"]["maxPWLength"],
        testString ,
        config["debugging"]["testDebug"])
       self.assertTrue(result)

    def test_stringMaxLength(self):
       # String Length of the maximum allowed from constant

       # Generate a random string with a length of the maximum threshold
       n = config["passwordDefaults"]["maxPWLength"]
       testString = ''.join(random.choices(string.ascii_uppercase + string.digits, k = n)) 

       result = length.passwordLengthCheck(config["passwordDefaults"]["minPWLength"],
        config["passwordDefaults"]["maxPWLength"],
        testString ,
        config["debugging"]["testDebug"])
       self.assertTrue(result)
    

if __name__ == '__main__':
    unittest.main()
