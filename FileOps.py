import os

''' 
Changed On: 20180811
Changed By: Nimit Rastogi
Changed: Added function  listFilesRecursive
'''

'''
For a given path as an input parameter, 
the funtion will return all the file names
present in this directory and all the 
sun directories, recursively
'''
def listFilesRecursive(path):
    files = []
    for (dirpath, filenames) in os.walk(path):
        for filename in filenames: 
            files.append(os.path.join(dirpath,filename))
    return files