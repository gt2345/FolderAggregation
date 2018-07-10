from os import walk
import os
import time

# take input from user
input = input('Please Enter the absolute path for a directory: ')
path = input

# dictionary to store modification times
# maxOfM and maxNumOfTime to store current most frequent modified time
dicTime = {}
maxOfM = None
maxNumOfTime = 0

# dictionary to store extensions
# maxOfE and maxNumOfExt to store current most frequent extension
dicExt = {}
maxOfE = None
maxNumOfExt = 0

# walk through given path
for (dirpath, dirnames, filenames) in walk(path):
    for file in (filenames + dirnames):
        try:
            filepath = dirpath + '/' + file
            # handle extensions
            if not os.path.isdir(filepath):
                extension = os.path.splitext(file)[-1]
                if extension is not '':
                    if extension in dicExt:
                        dicExt[extension] += 1
                    else:
                        dicExt[extension] = 1
                    # update maximum
                    if maxNumOfExt < dicExt[extension]:
                        maxOfE = extension
                        maxNumOfExt = dicExt[extension]

            # handle modification times
            statbuf = os.stat(filepath)
            mtime = time.strftime('%m/%d/%Y', time.gmtime(statbuf.st_mtime))
            if mtime in dicTime:
                dicTime[mtime] += 1
            else:
                dicTime[mtime] = 1
            # update maximum
            if maxNumOfTime < dicTime[mtime]:
                maxOfM = mtime
                maxNumOfTime = dicTime[mtime]
        except (FileNotFoundError, OSError):
            print('File Not Included {}'.format(filepath))


if maxOfM == None and maxOfE == None:
    print('This is not a valid directory.')
else:
    print('Day of the most modified is: {}'.format(maxOfM))
    print('Most popular extention is: {}'.format(maxOfE))
