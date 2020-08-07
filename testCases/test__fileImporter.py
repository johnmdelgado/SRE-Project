#!/usr/bin/python3
import os,sys,inspect
functionsDir = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))+ "/Functions" #functions Directory
print(functionsDir)
sys.path.insert(0, functionsDir) 
import fileImporter
import unittest
import yaml

with open("../configs/config.yaml", "r") as ymlfile:
    config = yaml.safe_load(ymlfile)


class PasswordCharactersTestCase(unittest.TestCase):

    # ========================================================================================
    # Program termininating test cases
    # ========================================================================================

    def test_filePathDoesNotExist(self):
        # should exit executing code
        testString = "./test.txt"
        self.assertRaises(TypeError, fileImporter.fileImporter, testString,config["debugging"]["testDebug"])

    def test_fileIsNotTxtFile(self):
        # should exit executing code
        testString = "../prohibitedPasswords/test.csv"
        self.assertRaises(TypeError, fileImporter.fileImporter, testString,config["debugging"]["testDebug"])

    # ========================================================================================
    # Valid filepaths returning map test cases
    # ========================================================================================

    def test_defaultFilePathFromConfig(self):
            # should exit executing code
            testString = config["passwordDefaults"]["excludedPWFilepath"]
            result = fileImporter.fileImporter(                        
                testString, 
                config["debugging"]["testDebug"])
            self.assertIsInstance(result, object)
            #self.assertRaises(SystemExit, fileImporter.fileImporter, testString,config["debugging"]["testDebug"])



if __name__ == '__main__':
    unittest.main()
