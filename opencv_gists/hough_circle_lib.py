from imports import *


img = cv2.imread('../pictures/test_circle_3.jpg')
kernel = np.ones((4,4)) / 16

filtered_img = cv2.filter2D(img,-1,kernel)
gray_img = cv2.cvtColor(filtered_img,cv2.COLOR_BGR2GRAY)

edge_img = cv2.Canny(gray_img,150,200)


circles = cv2.HoughCircles(edge_img,cv2.cv.CV_HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius = 20,maxRadius = 0)


for circle in circles[0]:
	cv2.circle(img,(circle[0],circle[1]),circle[2],(0,0,255),2)

plt.imshow(img)
plt.show()


	