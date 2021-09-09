import os
import sys
from pathlib import Path, PurePath


def createDirectory(directoryPath,directoryName):
    newPath = Path(directoryPath,directoryName)
    if not newPath.exists():
        print('here')
        newPath.mkdir()


if __name__ == '__main__':
    arguments = sys.argv[1:]
    #print(arguments)
    #path1 = arguments[0]
    for argument in arguments:
        tempPath = Path(argument)
        print(type(tempPath))
        print(tempPath.is_dir())
        if tempPath.is_dir():
            #tempPath.mkdir()

            createDirectory(tempPath,'newDirectory')
    '''
    tempPath = Path('../')
    temp = [x for x in tempPath.iterdir() if x.is_dir()]
    print(temp)
    test = PurePath('../','something')
    print(test)
    '''
    pass