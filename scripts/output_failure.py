#!/usr/bin/python
'''
FileName: output_failure.py
Author: John Delgado
Created Date: 8/5/2020
Version: 1.0 Initial Development

formatter for console output
'''
def output_failure(failed_validation, debug):
    # Debugging code
    if(debug):
        print()
        print("Failed Validation is: {} ".format(failed_validation))

    print("Did not pass {} check. Please see above reason".format(failed_validation))
