import os
from os.path import basename, dirname, isfile


def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        if '__pycache__' not in fullPath:
            if os.path.isdir(fullPath):
                allFiles = allFiles + getListOfFiles(fullPath)
            else:
                allFiles.append(fullPath)
                
    return allFiles

mod_paths = getListOfFiles(dirName=dirname(__file__))

all_modules = [
        f[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]

module_names = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]

print(
    ("INFO - "
    f"{', '.join(module_names)} - MODULES LOADED")
)
ALL_MODULES = sorted(all_modules)
__all__ = ALL_MODULES + ["ALL_MODULES"]
