import cv2 as cv

#Reading images
#img = cv.imread('photos/cat.jpg')
#cv.imshow('Cat',img)
#cv.waitKey(0)

########################################

#Reading videos
#0 for webcam 1 for other camera connected to your computer and so on
capture = cv.VideoCapture('videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Dog',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):#press d to end the video
        break

capture.release()
cv.destroyAllWindows()