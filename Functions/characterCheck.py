'''
FileName: characterCheck.py
Author: John Delgado
Created Date: 8/5/2020
Version: 1.0 Initial Development

There are probably a couple different ways valiate a string for ascii characters
    * Regex
    * built in string method .isAscii()

created it's own function for unit testing functionality and in case requirements change later. 

    Pros of choosing Regex
        * Powerful
        * multiple conditions can be checked at once
    Cons of choosing Regex
        * can get confusing quickly
        * could decrease performance if regex has too many checks

    Pros of choosing built in is.Ascii()
        * easier for readability and maintainability
    Cons of choosing is.Ascii()
        * needs at least python version 3.7
        * if requirements change will have to re-write this entire function again
        * After writing that last Con, I feel if I choose this method I'm going to regret it later. 

'''
import re  # regular expression module


def checkPasswordCharacters(password,regEx, debug):
    if(debug):
        print()
        print("Entering Ascii Character check")
        print("password is: {}".format(password))

    """
        Explanation from https://regex101.com/
        ^ asserts position at start of a line
            Match a single character present in the list below [ -~]+
                + Quantifier — Matches between one and unlimited times, as many times as possible, giving back as needed (greedy)
                -~ a single character in the range between   (index 32) and ~ (index 126) (case sensitive)
        $ asserts position at the end of a line
        Global pattern flags
            g modifier: global. All matches (don't return after first match)
            m modifier: multi line. Causes ^ and $ to match the begin/end of each line (not only begin/end of string)

        a single character in the range between(index 32) and ~ (index 126) (case sensitive) This will allow all printable characters (Ascii)
        added ^ and $ assertions after failed unit test: test_CombinationUnicodeString2
    """
    
    regExpression = regEx
    check = re.match(regEx,password)

    if(debug):
        print("Regex is: {}".format(regEx))
        print("Regular Expression check is: {}".format(check))

    if(check):
        if(debug):
            print("Password String {} contains only ascii characters".format(password))
        return True

    else:
        print("Password: '{}' contains Unicode or illegal characters. Ascii check has failed validation".format(password))
        return False
