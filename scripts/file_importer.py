'''
FileName: file_inporter.py
Author: John Delgado
Created Date: 8/7/2020
Version: 1.0 Initial Development

This will import a given file to use as a comparison for common passwords and then return a memory mapped object
'''

import mmap
import os
import sys



def file_importer(file_path,debug):
    if(debug):
        print("FileImporter function entered.") 
        print("File path being used:{}".format(filePath))

    if(not debug):
        sys.tracebacklimit=0


    path_exists = os.path.exists(file_path)
        
    if(not path_exists):       
        raise TypeError("Filepath does not exist. Please check path at: {}".format(filePath))

    if(not file_path.endswith(".txt")):
        raise TypeError("File provided from path: {} is not a .txt file. Please ensure the file is a newline delimited txt file".format(filePath))
    
    with open(file_path,"r") as file_to_search:
        mm = mmap.mmap(file_to_search.fileno(),
                      0,
                      access=mmap.ACCESS_READ)
        # Debugging code to check the correct values were getting written to this mmap
        # while True:
        #     line = mm.readline()
        #     if line == b'': break
        #     print(line.rstrip())
        # print(mm.readline())
        return mm
    

