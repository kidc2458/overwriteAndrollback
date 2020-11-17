import shutil
import os
import datetime

def overwrite(sourPath:str, destPath:str, logPath:str):
    logName = None
    f = None
    if logPath:
        try:
            if os.path.isfile(logPath):
                f = open(logPath,'a')
                logName = logPath
            elif os.path.isdir(logPath):
                #timestamp = '%Y%m%d%H%M%S'
                #logName = f'{logPath}/overwiteLog_{datetime.datetime.now().strftime(timestamp)}.log'
                logName = f'{logPath}/overwiteLog.log'
                f = open(logName,'w')
        except Exception as e:
            print(e)
            return

    if os.path.isfile(sourPath):    
        try:
            shutil.copyfile(sourPath,destPath)
            print(f'(Success) {sourPath} To {destPath}')
            f.write(f'{destPath}\n')
        except PermissionError as e:
            print(f'{e}을 읽을 수 없습니다.')
    elif os.path.isdir(sourPath):
        fileList = os.listdir(sourPath)
        try:
            os.mkdir(destPath)
        except:
            pass
        for fileName in fileList:
            sourFilePath = f'{sourPath}/{fileName}'
            destFilePath = f'{destPath}/{fileName}'
            overwrite(sourFilePath,destFilePath,logName)

    