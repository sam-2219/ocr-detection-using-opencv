import cv2
import pytesseract

#teseract is used for backend processing of images

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

#function to read and convert image from one channel to another one

img = cv2.imread('resource/testcaseragul.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#shape function is used to obtain size of the image

height,width,_ = img.shape

#output values are stored in a list
#image to boxes function is used to extract text from images

boxes = pytesseract.image_to_boxes(img)

#output values are used to draw boxes around it
#putText function is used to show the extracted image

for b in boxes.splitlines():
    b = b.split(' ')
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,height-y),(w,height-h),(0,0,200),3)
    cv2.putText(img,b[0],(x,height-y+29),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)


#function to show the processed image in new window

cv2.imshow('window',img)
cv2.waitKey(0)
