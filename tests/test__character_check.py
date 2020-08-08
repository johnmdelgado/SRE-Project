#!/usr/bin/python
'''
FileName: __test__test__character_check.py
Author: John Delgado
Created Date: 8/7/2020
Version: 1.0 Initial Development

This is the testing file for the character_check script
'''
import os
import sys
import inspect
functions_dir = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))+ "/scripts" #functions Directory
print(functions_dir)
sys.path.insert(0, functions_dir) 
import character_check
import unittest
import yaml

with open("../configs/config.yaml", "r") as ymlfile:
    config = yaml.safe_load(ymlfile)


class password_characters_test_case(unittest.TestCase):

    # ========================================================================================
    # False test cases
    # ========================================================================================

    def test_empty_string(self):
        # empty String
        test_string = ""
        result = character_check.check_password_characters(test_string,            
                                                          config["password_defaults"]["password_regex"], 
                                                          config["debugging"]["test_debug"])
        self.assertFalse(result)

    def test_chineese_unicode_string(self):
        # Unicode only test
        test_string = "语言处理"
        result = character_check.check_password_characters(test_string,            
                                                          config["password_defaults"]["password_regex"], 
                                                          config["debugging"]["test_debug"])
        self.assertFalse(result)

    def test_combination_unicode_string(self):
        # combination of unicode and ascii
        test_string = "语言处理 is Language Processing in Chineese"
        result = character_check.check_password_characters(test_string,            
                                                          config["password_defaults"]["password_regex"], 
                                                          config["debugging"]["test_debug"])
        self.assertFalse(result)

    def test_combination_unicode_string2(self):
        # combination of unicode and ascii
        # example from https://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-test.txt
        test_string = "You should see the Greek word 'kosme': κόσμε "
        result = character_check.check_password_characters(test_string,            
                                                          config["password_defaults"]["password_regex"], 
                                                          config["debugging"]["test_debug"])
        self.assertFalse(result)

    # ========================================================================================
    # True test cases
    # ========================================================================================

    def test_space_as_string(self):
        # space as String
        test_string = " "
        result = character_check.check_password_characters(test_string,            
                                                          config["password_defaults"]["password_regex"], 
                                                          config["debugging"]["test_debug"])
        self.assertTrue(result)

    def test_ascii_string(self):

        test_string = "simpleAsciiString"
        result = character_check.check_password_characters(test_string,            
                                                          config["password_defaults"]["password_regex"], 
                                                          config["debugging"]["test_debug"])
        self.assertTrue(result)

    def test_ascii_string_with_spaces(self):

        test_string = "simple Ascii String"
        result = character_check.check_password_characters(test_string,            
                                                          config["password_defaults"]["password_regex"], 
                                                          config["debugging"]["test_debug"])
        self.assertTrue(result)

    def test_ascii_string_with_special_characters(self):

        test_string = "Th1sT3$th@s$p@c3$&$peci@lCharacters"
        result = character_check.check_password_characters(test_string,            
                                                          config["password_defaults"]["password_regex"], 
                                                          config["debugging"]["test_debug"])
        self.assertTrue(result)

    def test_ascii_string_with_special_characters_and_spaces(self):

        test_string = "Th1s T3$t h@s $p@c3$ & $peci@l Characters"
        result = character_check.check_password_characters(test_string,            
                                                          config["password_defaults"]["password_regex"], 
                                                          config["debugging"]["test_debug"])
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
