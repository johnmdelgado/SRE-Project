#!/usr/bin/python
def outputFailure(failedValidation, debug):
    # Debugging code
    if(debug):
        print()
        print("Failed Validation is: {} ".format(failedValidation))

    print("Did not pass {} check. Please see above reason".format(failedValidation))
