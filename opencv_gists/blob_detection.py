from imports import *


img = cv2.imread('../pictures/hand_pic.JPG')
dummy = img.copy()
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,img_new = cv2.threshold(img,50,255,0)



#params = cv2.SimpleBlobDetector_Params()
#params.filterByConvexity = True
#params.minConvexity = 0.25


#detector = cv2.SimpleBlobDetector()

#keypoints = detector.detect(img_new)

#dummy = cv2.drawKeypoints(img_new,keypoints,np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.imshow(dummy)
plt.show()

