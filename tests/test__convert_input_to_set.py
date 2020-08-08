#!/usr/bin/python
'''
FileName: __test__convert_input_to_set.py
Author: John Delgado
Created Date: 8/7/2020
Version: 1.0 Initial Development

This is the testing file for the convert_input_to_set script
'''
import os
import sys
import inspect
functions_dir = os.path.dirname(os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))) + "/scripts"  # scripts Directory
print(functions_dir)
sys.path.insert(0, functions_dir)
import yaml
import unittest
import convert_input_to_set


with open("../configs/config.yaml", "r") as ymlfile:
    config = yaml.safe_load(ymlfile)


class convert_input_test_case(unittest.TestCase):
    # ========================================================================================
    # Program termininating test cases
    # ========================================================================================
    def test_empty_input(self):
        # empty String
        test_input = ""
        self.assertRaises(Exception, convert_input_to_set.convert_input_to_set, test_input, config["debugging"]["test_debug"])

    # ========================================================================================
    # Valid input returning a set
    # ========================================================================================
    def test_input_from_test_file(self):
        test_file = open(config["testing"]["sample_txt_file"],"r")
        result = convert_input_to_set.convert_input_to_set(test_file, 
                                                          config["debugging"]["test_debug"])
        test_file.close()

        self.assertIsInstance(result, object)

if __name__ == '__main__':
    unittest.main()