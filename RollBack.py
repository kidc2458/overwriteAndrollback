import subprocess
import os

def rollback(sourPath:str, fileListFile:str):
    if not os.path.isfile(fileListFile):
        return
    if not os.path.isdir(sourPath):
        return
    f = open(fileListFile,'r')
    fileList = f.read().split('\n')
    for filePath in fileList:
        if not os.path.isfile(filePath):
            continue
        try:
            output = subprocess.Popen(['svn', 'status',filePath],stdout=subprocess.PIPE,stderr=subprocess.PIPE ,shell=False,universal_newlines=True)
            #output = subprocess.Popen(['ATTRIB',filePath],stdout=subprocess.PIPE ,shell=False,universal_newlines=True)
            if not output.stdout.read():
                os.remove(filePath)
                print(f'Delete {filePath}')
            else:
                subprocess.Popen(['svn', 'revert','-R',filePath],stdout=subprocess.PIPE,stderr=subprocess.PIPE ,shell=False,universal_newlines=True)
                print(f'Revert {filePath}')
        except Exception as e:
            print(e)