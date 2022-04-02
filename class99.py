'''import os
import shutil

source="./project99/pro/file1.txt"
destination="./project99/"
#dst=shutil.copy(source,destination)
dest=shutil.move(source,destination)


#path="./sampleClass.txt"

#list1=os.path.splitext(path)
#os.mkdir("./project99")
#print("file name : ",list1[0])
#print("Extension :",list1[1])'''


import shutil
import os
source=input("Enter source folder name")
destination=input("enter destination folder name")
source=source+"/"
destination=destination+"/"

listoffiles=os.listdir(source)

for file in listoffiles:
    shutil.move((source+file),destination)

