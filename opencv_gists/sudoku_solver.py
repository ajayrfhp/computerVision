from imports import *
img = cv2.imread('../pictures/sudoku.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img = cv2.GaussianBlur(img,(7,7),0)

img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
img = cv2.morphologyEx(img,cv2.MORPH_CLOSE,np.ones((2,2)))
img = cv2.bitwise_not(img)
img_bigline = np.zeros(img.shape) 

contours,hierachy = cv2.findContours(img.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours.sort(key = lambda x:cv2.contourArea(x),reverse = True)

img_old = img.copy()

#cv2.drawContours(img,contours[1],-1,(255,255,255),15)
a = np.array(contours[1])
x_min,x_max =  a[0:,0,0].min(),a[0:,0,0].max()
y_min,y_max =  a[0:,0,1].min(),a[0:,0,1].max()
cv2.rectangle(img,(x_min,y_min),(x_max,y_max),(255,255,255),15)





plt.imshow(img,cmap = 'gray')
plt.show()

'''

for i in range(9):
	
	x,y,w,h = cv2.boundingRect(contours[i+1])
	e =  0

	sub_rect = contours[1]
	#plt.imshow(sub_rect,cmap = 'gray')
	#plt.show()

#cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),15)
'''




