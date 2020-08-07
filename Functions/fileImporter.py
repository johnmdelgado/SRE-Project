import mmap
import os
import sys

#sys.tracebacklimit=0

def fileImporter(filePath,debug):
    if(debug):
        print("FileImporter function entered.") 
        print("File path being used:{}".format(filePath))


    pathExists = os.path.exists(filePath)
        
    if(not pathExists):       
        raise TypeError("Filepath does not exist. Please check path at: {}".format(filePath))

    if(not filePath.endswith(".txt")):
        raise TypeError("File provided from path: {} is not a .txt file. Please ensure the file is a newline delimited txt file".format(filePath))
    
    with open(filePath,"r") as fileToSearch:
        mm = mmap.mmap(fileToSearch.fileno(), 0, access=mmap.ACCESS_READ)
        # mmap.mmap(fileToSearch.fileno(), 0)
        return mm
    

