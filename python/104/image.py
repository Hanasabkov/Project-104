import cv2
img = cv2.imread("solar-system.jpg")
#rocket=img[120:360,400:500]
#img[0:240,500:600]=rocket
text_toshow="The Solar System"
cv2.putText(img,text_toshow,(20,220),fontFace=cv2.FONT_ITALIC,fontScale=1,color=(0,0,255))
cv2.imshow("output",img)
cv2.waitKey(0)