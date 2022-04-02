
import os 
import shutil
import time


def main():
    deleted_folders_count=0
    deleted_files_count=0
    path="./"
    days=30
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        for root,folders,files in os.walk(path):
            if seconds>=getfileorfolderage(root):
                removefolder(root)
                deleted_folders_count+=1
                break
            else:
                for folder in folders:
                    folder_path=os.path.join(root,folder)
                    if seconds>=getfileorfolderage(folder_path):
                        removefolder(folder_path)
                        deleted_folders_count+=1
                for file in files:
                    file_path=os.path.join(root,file)
                    if seconds>=getfileorfolderage(file_path):
                        removefile(file_path)
                        deleted_files_count+=1
    else:
        print("Not found")

    print(deleted_folders_count)
    print(deleted_files_count)
    


def removefolder(path):
    if not shutil.rmtree(path):
        print("path removed successfully")
    else:
        print("unable to delete the path")


def removefile(path):
    if not os.remove(path):
        print("file removed successfully")
    else:
        print("unable to delete the file")

def getfileorfolderage(path):
    ctime=os.stat(path).st_ctime
    return ctime

if __name__=="__main__":
    main()




        








