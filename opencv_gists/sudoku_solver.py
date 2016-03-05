from imports import *
img = cv2.imread('../pictures/sudoku.jpg')
img_color = img.copy()
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_color = cv2.cvtColor(img_color,cv2.COLOR_BGR2RGB)

img = cv2.GaussianBlur(img,(7,7),0)
img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
img = cv2.morphologyEx(img,cv2.MORPH_CLOSE,np.ones((2,2)))
img = cv2.bitwise_not(img)
img_bigline = np.zeros(img.shape) 

contours,hierachy = cv2.findContours(img.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
contours.sort(key = lambda x:cv2.contourArea(x),reverse = True)

approx = cv2.approxPolyDP(contours[0],0.1*cv2.arcLength(contours[0],True),True)
M = cv2.moments(contours[0])
centroid_x = int(M['m10']/M['m00'])
centroid_y = int(M['m01']/M['m00'])
a_x,a_y,b_x,b_y,c_x,c_y,d_x,d_y = 0,0,0,0,0,0,0,0
best_a_x,best_b_x,best_c_y,best_d_y = sys.maxint,0,sys.maxint,0

for i in range(len(approx)):
	this_x = approx[i][0][0]
	this_y = approx[i][0][1]
	if( this_x < best_a_x and this_x < centroid_x and this_y < centroid_y ):
		a_x = this_x
		a_y = this_y
		best_a_x = this_x
	if (  this_x > best_b_x and this_x > centroid_x and this_y < centroid_y  ):
		b_x = this_x
		b_y = this_y
		best_b_x = this_x

	if( this_y < best_c_y and this_x < centroid_x and this_y > centroid_y ):
		c_x = this_x
		c_y = this_y
		best_y = this_y		 
	if( this_y > best_d_y and this_x > centroid_x and this_y > centroid_y ):
		d_x = this_x
		d_y = this_y
		best_y = this_y

edge_length = max(b_x -a_x,d_y-b_y,d_x-c_x,c_y-a_y)
pts_initial = np.float32([[a_x,a_y],[b_x,b_y],[c_x,c_y],[d_x,d_y]])
pts_final = np.float32([[0,0],[edge_length,0],[0,edge_length],[edge_length,edge_length]])
transform_Matrix = cv2.getPerspectiveTransform(pts_initial,pts_final)
img = cv2.warpPerspective(img,transform_Matrix,(edge_length,edge_length))
plt.imshow(img,cmap = 'gray')
plt.show()



				
	




