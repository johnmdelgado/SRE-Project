#!/usr/bin/python
'''
FileName: test__common_password.py
Author: John Delgado
Created Date: 8/5/2020
Version: 1.0 Initial Development

This script will test the functionality of  common_password

'''
import os
import sys
import inspect
functions_dir = os.path.dirname(os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))) + "/scripts"  # scripts Directory
print(functions_dir)
sys.path.insert(0, functions_dir)
import mmap
import common_password
import unittest
import yaml



with open("../configs/config.yaml", "r") as ymlfile:
    config = yaml.safe_load(ymlfile)

with open(config["testing"]["sample_excluded_pw_filepath"], "r") as exluded_passwords:
    mm = mmap.mmap(exluded_passwords.fileno(),
                   0,
                   access=mmap.ACCESS_READ)


class common_password_test_case(unittest.TestCase):

    # ========================================================================================
    # true test cases
    # ========================================================================================
    def test_password_is_common(self):
        test_strings = ("stalingrad", "squad", "spycams", "spooky1", "spokane")
        
        for line in test_strings:
            result = common_password.common_password_check(line,
                                                        mm,
                                                        config["output_settings"]["output_valid_passwords"],
                                                        config["debugging"]["test_debug"])
            self.assertTrue(result)

    # ========================================================================================
    # false test cases
    # ========================================================================================
    def test_password_is__not_common(self):
        test_string = ("WhoaThisIsACrazyUniquePassword")
        result = common_password.common_password_check(test_string,
                                                    mm,
                                                    config["output_settings"]["output_valid_passwords"],
                                                    config["debugging"]["test_debug"])
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
