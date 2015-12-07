from imports import *


img = cv2.imread('../pictures/football.jpg')
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edge_img = cv2.Canny(gray_img,50,150)
cv2.imshow('image',edge_img)
cv2.waitKey(0)

lines = cv2.HoughLinesP(edge_img,1,np.pi/180,40,10,50)
print lines
for x1,y1,x2,y2 in lines[0]:
	
	cv2.line(img,(x2,y2),(x1,y1),(0,0,255),1)
	
cv2.imwrite('../output/houghlines3.jpg',img)	