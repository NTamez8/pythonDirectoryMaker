import os
import sys
from pathlib import Path, PurePath


def createDirectory(directoryPath,directoryName):
    newPath = Path(directoryPath,directoryName)
    if not newPath.exists():
        newPath.mkdir()


if __name__ == '__main__':
    arguments = sys.argv[1:]
    if not len(arguments) % 2 == 0:
        print("To few arguments")
        exit()
    for x in range(0,len(arguments),2):
        tempPath = Path(arguments[x])
        if tempPath.is_dir():

            createDirectory(tempPath,arguments[x+1])
    pass