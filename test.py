import cv2

def takeSnapShot():
    videocaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        result,frame = videocaptureObject.read()
        cv2.imwrite('pic.png',frame)
        result = False

    videocaptureObject.release()
    cv2.destroyAllWindows()

takeSnapShot()