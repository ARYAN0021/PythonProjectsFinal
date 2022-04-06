from os import access
from tkinter import image_names
import cv2
import dropbox
import time
import random
start_time=time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        #print(ret,frame)
        cv2.imwrite(img_name,frame)
        start_time=time.time()
        result=False
    return img_name
    
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    
def upload_files(image_name):
    access_token="sl.BFNXVhLcVxzWNu4AWyBuMBw9q07HWCeS1ifaeAhkH5wibVA8iwoLjtu8wVC-BWZ_dTMYCduOJ1NHUYhq1GMEDxuPeoUiGHtmbkwJuStlCNJnL8wtjFjws_HXPC7eISi4P6PNqoqvzzE"
    file= image_name
    file_from=file
    file_to="/ary/"+(image_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,"rb") as f:
        dbx.file_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time() - start_time) >= 5):
            name=take_snapshot()
            upload_files(name)

main()
