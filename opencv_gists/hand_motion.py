from imports import *

img = cv2.imread('../pictures/hand_pic.JPG')
dummy = img.copy()
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 11, 1)


ret,img = cv2.threshold(img,50,255,0)





contours, heirachy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(dummy,contours,-1,(0,0,255),2)

cnt = contours[0]
M = cv2.moments(cnt)

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

cv2.circle(dummy,(cx,cy),2,(0,0,255),-1)

plt.imshow(dummy,cmap = 'gray')
plt.show()



