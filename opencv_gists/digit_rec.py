from imports import *

img = cv2.imread('../pictures/characters.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, img = cv2.threshold(img, 90, 255, cv2.THRESH_BINARY_INV) 

contours,heirachy = cv2.findContours(img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


rects = [ cv2.boundingRect(c) for c in contours ]
print rects


plt.imshow(img,cmap = 'gray')
plt.show()