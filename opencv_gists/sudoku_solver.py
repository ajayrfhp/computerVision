from imports import *
img = cv2.imread('../pictures/sudoku.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img = cv2.GaussianBlur(img,(7,7),0)

img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
img = cv2.morphologyEx(img,cv2.MORPH_CLOSE,np.ones((2,2)))
img = cv2.bitwise_not(img)
img_bigline = np.zeros(img.shape) 


detector = cv2.SimpleBlobDetector()

#keypoints = detector.detect(img)
#keypoints.sort(key = lambda x:x.size,reverse = True)
#img = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)



contours,hierachy = cv2.findContours(img.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
contours.sort(key = lambda x:cv2.contourArea(x),reverse = True)
cv2.drawContours(img_bigline,contours[0:10],-1,(255,255,255),3)



plt.imshow(img_bigline,cmap = 'gray')
plt.show()
