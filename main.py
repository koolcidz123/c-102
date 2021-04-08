import cv2
import time
import dropbox
import random

startTime = time.time()

def take_snapshot():
    number = random.randint(0, 100000)
    videoCaptureobject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureobject.read()
        imgName = "img"+str(number)+".png"
        cv2.imwrite(imgName, frame)
        startTime = time.time()
        result = False
    videoCaptureobject.release()
    cv2.destroyAllWindows()
    return imgName

def upload_files(imgName):
    accessToken = "sl.Aul6C8rbUZcyZ7-aJIuEenMqtuz_ZvbyXdbRF5dltLuSwbHK-lgelte4rtU94RziCwKEiAcOUqVRdILQ9Tovr8gZ1HqZS9mQfI2vGmWQdrY-mPxZCtsYDHI5AxtfQ-ls6ejN3bKjj7k"
    file = imgName
    fileto = "/testFolder/" + (imgName)
    dbx = dropbox.Dropbox(accessToken)
    with open(file, 'rb') as f:
        dbx.files_upload(f.read(), fileto, mode=dropbox.files.WriteMode.overwrite)
    print("File Uploaded. Security!")

def main():
    while True:
        if((time.time() - startTime) >= 5):
            image = take_snapshot()
            upload_files(image)


main()


