import os

def renameFiles():
    fileList = os.listdir(r"C:\Users\sbaxt\Downloads\prank\prank")
    print (fileList)
    savedPath = os.getcwd()
    os.chdir(r"C:\Users\sbaxt\Downloads\prank\prank")
    for fileName in fileList:
        os.rename(fileName, fileName.translate(None, "0123456789"))
    os.chdir(savedPath)
                  
renameFiles()
