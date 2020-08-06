#!/usr/bin/python
import os,sys,inspect
functionsDir = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))+ "/Functions" #functions Directory
print(functionsDir)
sys.path.insert(0, functionsDir) 
import characterCheck
import unittest
import yaml

with open("../configs/config.yaml", "r") as ymlfile:
    config = yaml.safe_load(ymlfile)


class PasswordCharactersTestCase(unittest.TestCase):

    # ========================================================================================
    # False test cases
    # ========================================================================================

    def test_emptyString(self):
        # empty String
        testString = ""
        result = characterCheck.checkPasswordCharacters(
            testString,            
            config["passwordDefaults"]["PasswordRegEx"], 
            config["debugging"]["testDebug"])
        self.assertFalse(result)

    def test_chineeseUnicodeString(self):
        # Unicode only test
        testString = "语言处理"
        result = characterCheck.checkPasswordCharacters(
            testString,
            config["passwordDefaults"]["PasswordRegEx"],
            config["debugging"]["testDebug"])
        self.assertFalse(result)

    def test_CombinationUnicodeString(self):
        # combination of unicode and ascii
        testString = "语言处理 is Language Processing in Chineese"
        result = characterCheck.checkPasswordCharacters(
            testString,
            config["passwordDefaults"]["PasswordRegEx"],
            config["debugging"]["testDebug"])
        self.assertFalse(result)

    def test_CombinationUnicodeString2(self):
        # combination of unicode and ascii
        # example from https://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-test.txt
        testString = "You should see the Greek word 'kosme': κόσμε "
        result = characterCheck.checkPasswordCharacters(
            testString,
            config["passwordDefaults"]["PasswordRegEx"],
            config["debugging"]["testDebug"])
        self.assertFalse(result)

    # ========================================================================================
    # True test cases
    # ========================================================================================

    def test_spaceAsString(self):
        # space as String
        testString = " "
        result = characterCheck.checkPasswordCharacters(
            testString,
            config["passwordDefaults"]["PasswordRegEx"],
            config["debugging"]["testDebug"])
        self.assertTrue(result)

    def test_asciiString(self):

        testString = "simpleAsciiString"
        result = characterCheck.checkPasswordCharacters(
            testString,
            config["passwordDefaults"]["PasswordRegEx"],
            config["debugging"]["testDebug"])
        self.assertTrue(result)

    def test_asciiStringWithSpaces(self):

        testString = "simple Ascii String"
        result = characterCheck.checkPasswordCharacters(
            testString,
            config["passwordDefaults"]["PasswordRegEx"],
            config["debugging"]["testDebug"])
        self.assertTrue(result)

    def test_asciiStringWithSpecialCharactersAndSpaces(self):

        testString = "Th1sT3$th@s$p@c3$&$peci@lCharacters"
        result = characterCheck.checkPasswordCharacters(
            testString,
            config["passwordDefaults"]["PasswordRegEx"],
            config["debugging"]["testDebug"])
        self.assertTrue(result)

    def test_asciiStringWithSpecialCharactersAndSpaces(self):

        testString = "Th1s T3$t h@s $p@c3$ & $peci@l Characters"
        result = characterCheck.checkPasswordCharacters(
            testString,
            config["passwordDefaults"]["PasswordRegEx"],
            config["debugging"]["testDebug"])
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
