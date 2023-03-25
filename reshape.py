import cv2 as cv

img = cv.imread('photos/cat.jpg')
cv.imshow('Cat',img)

def rescaleFrame(frame, scale=0.75):
    # works for images, videos and live videos
    width= int(frame.shape[1] * scale)
    height= int(frame.shape[0] * scale)
    dimensions = width, height
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #only works for live videos
    capture.set(3,width)
    capture.set(4,height)

resized_image= rescaleFrame(img)
cv.imshow('Cat_Resized',resized_image)
cv.waitKey(0)


capture = cv.VideoCapture('videos/dog.mp4')
while True:
    isTrue, frame = capture.read()

    frame_resized= rescaleFrame(frame,scale=0.2)

    cv.imshow('Video',frame)
    cv.imshow('Video_Resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):#press d to end the video
        break

capture.release()
cv.destroyAllWindows()