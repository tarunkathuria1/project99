import os
import shutil
import time

source=input('enter soure folder name:-')
destination=input('enter destination folder name :-')

source=source + '/'
destination=destination + '/'

list_of_file = os.listdir(source)
for file in list_of_file:
    shutil.copy((source+file), destination)

    ctime = os.stat(path).st_ctime
    return ctime