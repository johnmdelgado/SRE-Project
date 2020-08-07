import mmap
import os
import sys



def fileImporter(filePath,debug):
    if(debug):
        print("FileImporter function entered.") 
        print("File path being used:{}".format(filePath))

    if(not debug):
        sys.tracebacklimit=0


    pathExists = os.path.exists(filePath)
        
    if(not pathExists):       
        raise TypeError("Filepath does not exist. Please check path at: {}".format(filePath))

    if(not filePath.endswith(".txt")):
        raise TypeError("File provided from path: {} is not a .txt file. Please ensure the file is a newline delimited txt file".format(filePath))
    
    with open(filePath,"r") as fileToSearch:
        mm = mmap.mmap(fileToSearch.fileno(), 0, access=mmap.ACCESS_READ)
        # Debugging code to check the correct values were getting written to this mmap
        # while True:
        #     line = mm.readline()
        #     if line == b'': break
        #     print(line.rstrip())
        # print(mm.readline())
        return mm
    

