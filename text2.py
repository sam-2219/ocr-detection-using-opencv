import cv2
import pytesseract

#teseract is used for backend processing of images

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

#function to read and convert image from one channel to another one

img = cv2.imread('resource/testcasesam1.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#shape function is used to obtain size of the image

height,width,_ = img.shape

#output values are stored in a list
#image to data function is used to extract text from images

boxes = pytesseract.image_to_data(img)

#output values are used to draw boxes around it
#putText function is used to show the extracted image

for x,b in enumerate(boxes.splitlines()):
    if x!=0:
        b = b.split()
        if len(b) == 12:
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,200),3)
            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,250,255),2)

#function to show the processed image in new window

cv2.imshow('window',img)
cv2.waitKey(0)