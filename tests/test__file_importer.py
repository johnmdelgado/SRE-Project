#!/usr/bin/python3
'''
FileName: test__file_importer.py
Author: John Delgado
Created Date: 8/7/2020
Version: 1.0 Initial Development

This is the testing file for the file_importer script
'''
import os
import sys
import inspect
functions_dir = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))+ "/scripts" #scripts Directory
print(functions_dir)
sys.path.insert(0, functions_dir) 
import file_importer
import unittest
import yaml

with open("../configs/config.yaml", "r") as ymlfile:
    config = yaml.safe_load(ymlfile)


class password_characters_test_case(unittest.TestCase):

    # ========================================================================================
    # Program termininating test cases
    # ========================================================================================

    def test_file_path_does_not_exist(self):
        # should exit executing code
        test_string = "./test.txt"
        self.assertRaises(Exception, file_importer.file_importer, test_string,config["debugging"]["test_debug"])

    def test_file_is_not_txt_file(self):
        # should exit executing code
        testString = "../data/test.csv"
        self.assertRaises(Exception, file_importer.file_importer, testString,config["debugging"]["test_debug"])

    # ========================================================================================
    # Valid filepaths returning map test cases
    # ========================================================================================

    def test_default_file_path_from_config(self):
            # should exit executing code
            testString = config["testing"]["sample_excluded_pw_filepath"]
            result = file_importer.file_importer(testString, 
                                                config["debugging"]["test_debug"])
            self.assertIsInstance(result, object)



if __name__ == '__main__':
    unittest.main()
