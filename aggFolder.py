import os
import time
import itertools


# take input from user
input = input('Please Enter the absolute path for a directory: ')
# input = '/Users/root1/Documents/unixstuff'

# dictionary to store modification times
# maxOfM: [current most frequent modified time, track #times]
dicTime = {}
maxOfM = [None, 0]

# dictionary to store extensions
# maxOfE: [current most frequent extension, track #times]
dicExt = {}
maxOfE = [None, 0]


# store modification time in dicTime
# if file: store extension in dicExt
def fileHandler(filePath):
    print('File Included: {}'.format(filePath))
    if os.path.exists(filePath):
        # handle modification times
        statbuf = os.stat(filePath)
        mtime = time.strftime('%m/%d/%Y', time.gmtime(statbuf.st_mtime))
        if mtime in dicTime:
            dicTime[mtime] += 1
        else:
            dicTime[mtime] = 1
        # update maximum
        if maxOfM[1] < dicTime[mtime]:
            maxOfM[0] = mtime
            maxOfM[1] = dicTime[mtime]

        # handle extensions
        if not os.path.isdir(filePath):
            extension = os.path.splitext(filePath)[-1]
            if extension is not '':
                if extension in dicExt:
                    dicExt[extension] += 1
                else:
                    dicExt[extension] = 1
                # update maximum
                if maxOfE[1] < dicExt[extension]:
                    maxOfE[0] = extension
                    maxOfE[1] = dicExt[extension]



# walk through given path
def myWalk(input):
    if os.path.exists(input):
        dirs = []
        try:
            scandir_it = os.scandir(input)
            with scandir_it:
                while True:
                    try:
                        entry = next(scandir_it)
                    except StopIteration:
                        break

                    fileHandler(os.path.join(input, entry))
                    if os.path.isdir(entry):
                        dirs.append(entry)

                yield dirs
                for dirname in dirs:
                    yield from myWalk(os.path.join(input, dirname))


        except PermissionError:
            print('File Not Included: {}'.format(input))



for x in myWalk(input):
    pass



if maxOfM[0] is None and maxOfE[0] is None:
    print('This is not a valid directory.')
else:
    print('Day of the most modified is: {}'.format(maxOfM[0]))
    print('Most popular extention is: {}'.format(maxOfE[0]))
