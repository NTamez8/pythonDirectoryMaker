import sys
from pathlib import Path, PurePath


def createDirectory(directoryPath,directoryName):
    '''
    directoryPath: the path where the directory should be made
    directoryName: the name of the new directory
    '''
    newPath = Path(directoryPath,directoryName)
    if not newPath.exists():
        newPath.mkdir(parents=True)

if __name__ == '__main__':
    '''
    assumes that arguments are passed in as pairs
    so path then folder name
    '''
    arguments = sys.argv[1:]
    if not len(arguments) % 2 == 0:
        print("To few arguments")
        exit()
    for x in range(0,len(arguments),2):
        tempPath = Path(arguments[x])
        if tempPath.is_dir():
            createDirectory(tempPath,arguments[x+1])
    pass
