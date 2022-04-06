import cv2
def take_snapshot():
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        cv2.imwrite("picture.jpg",frame)
        print(ret,frame)
        result=False
    videoCaptureObject.release()
    cv2.destroyAllWindows()

take_snapshot()
