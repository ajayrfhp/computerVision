from imports import *
img = cv2.imread('../pictures/completecircle.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


img = cv2.bitwise_not(img)
params = cv2.SimpleBlobDetector_Params()

params.filterByConvexity = 1
params.minConvexity = 0.95

params.filterByArea = 1
params.minArea = 140

detector = cv2.SimpleBlobDetector(params)
keypoints = detector.detect(img)


for point in keypoints:
	cv2.circle(img,(int(point.pt[0]),int(point.pt[1])),7,(255,255,255),-1)


img = cv2.bitwise_not(img)
ret,img = cv2.threshold(img.copy(),127,255,cv2.THRESH_BINARY)





if(len(keypoints) != 48):
	print 'error disfiguration'

plt.imshow(img,cmap = 'gray')
plt.show()