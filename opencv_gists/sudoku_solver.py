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
'''
rect = cv2.minAreaRect(contours[0])
box = cv2.cv.BoxPoints(rect)
box = np.int0(box)
cv2.drawContours(img,[box],0,(255,255,255),2)

c_x,c_y = rect[0]
w,h = rect[1]

s_x,s_y = (c_x - w/2,c_y - h/2)
d_x,d_y = (c_x + w/2,c_x + h/2)
e = 5
#img = img[s_y-e:d_y+e,s_x-e:d_x+e]
'''


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


img_poly = np.zeros(img.shape)
cv2.line(img_poly,(a_x,a_y),(b_x,b_y),(255,255,255),2)
cv2.line(img_poly,(a_x,a_y),(c_x,c_y),(255,255,255),2)
cv2.line(img_poly,(c_x,c_y),(d_x,d_y),(255,255,255),2)
cv2.line(img_poly,(d_x,d_y),(b_x,b_y),(255,255,255),2)
plt.imshow(img_poly,cmap = 'gray')
plt.show()



'''
for j in range(0,1):
	for i in range(0,1):
		img_new = img.copy()
		rect = cv2.minAreaRect(contours[j*3 + i + 1])
		box = cv2.cv.BoxPoints(rect)
		box = np.int0(box)
		cv2.drawContours(img_new,[box],0,(255,255,255),-1)
		img_diff = img_new - img
		w,h = (d_x - s_x)/3,(d_y - s_y)/3
		
		img_diff = img_diff[(-15+s_y + (2-j)*h):(s_y + (2-j+1)*h),(-15+s_x + (2-i)*w):(s_x + (2-i+1)*w)]
		img_diff = cv2.bitwise_not(img_diff)
		contours,hierachy = cv2.findContours(img.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
		contours.sort(key = lambda x:cv2.contourArea(x),reverse = True)
		


		img_diff = cv2.Canny(img_diff,50,150)
		lines = cv2.HoughLinesP(img_diff,1,np.pi/180,10,50,10)
		img_blah = np.zeros(img_diff.shape)

		for x1,y1,x2,y2 in lines[0]:
			cv2.line(img_blah,(x1,y1),(x2,y2),(255,255,255),2)

		plt.imshow(img_blah,cmap = 'gray')
		plt.show()

		for i in range(3):
			for j in range(3):
				digit_r,digit_c = img_diff.shape[0]/3,img_diff.shape[1]/3,
				digit = img_diff[i*digit_r:(i+1)*digit_r,j*digit_c:(j+1)*digit_c]
'''

				#plt.imshow(digit,cmap = 'gray')
				#plt.show()	
				
	




