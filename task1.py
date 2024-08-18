import open
import cv2

def getcontours(img):
    contours, hierarchy= cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        cv2.drawContours(imgcon, cnt, -1, (300,100, 200), 3)
        peri=cv2.arcLength(cnt,True)
        approx=cv2.approxPolyDP(cnt, 0.02*peri, True)
        print(len(approx))
        corner=len(approx)
        x, y, w, h=cv2.boundingRect(approx)
        cv2.rectangle(imgcon, (x, y), (x+w, y+h), (0, 0, 0), 2)
        if corner==3:
            objecttype='TRIANGLE'
        elif corner==4:
            if w/h==1:
                objecttype='SQUARE'
            else:
                objecttype='RECTANGLE'
        elif corner==5:
            objecttype='PENTAGON'
        elif corner==6:
            objecttype = 'HEXAGON'
        else:
            objecttype = 'CIRCLE'
        cv2.putText(imgcon, objecttype, (x, y-5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

img= cv2.imread('shapes.png')
imgcon=img.copy()
imggray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgblur=cv2.GaussianBlur(imggray,(7, 7),1)
imgcanny=cv2.Canny(imgblur, 50, 50)
getcontours(imgcanny)

cv2.imshow('image', img)
cv2.imshow('Gray Image', imggray)
cv2.imshow('BLUR Image', imgblur)
cv2.imshow('Canny Image', imgcanny)
cv2.imshow('Contour image', imgcon)

cv2.waitKey(0)
cv2.destroyAllWindows()
