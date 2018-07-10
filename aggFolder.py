from os import walk
import os
import time

input = input('Please Enter the absolute path for a directory: ')
path = input
dicTime = {}
maxOfM = None
maxNumOfTime = 0
dicExt = {}
maxOfE = None
maxNumOfExt = 0
for (dirpath, dirnames, filenames) in walk(path):
    for file in (filenames + dirnames):
        try:
            filepath = dirpath + '/' + file
            if not os.path.isdir(filepath):
                extention = os.path.splitext(file)[-1]
                if extention is not '':
                    if extention in dicExt:
                        dicExt[extention] += 1
                    else:
                        dicExt[extention] = 1
                    if maxNumOfExt < dicExt[extention]:
                        maxOfE = extention
                        maxNumOfExt = dicExt[extention]

            statbuf = os.stat(filepath)
            mtime = time.strftime('%m/%d/%Y', time.gmtime(statbuf.st_mtime))
            if mtime in dicTime:
                dicTime[mtime] += 1
            else:
                dicTime[mtime] = 1

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
