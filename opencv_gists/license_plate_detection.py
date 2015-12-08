from imports import *
img = cv2.imread('../pictures/car.jpg')
img = ndimage.rotate(img,-2)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
org_img = img.copy()
# convert to gray scale



# assumption is that we know size of the number plate, kernel size is to be changed depending upon that.
kernel = np.ones((10,10))
big_kernel = np.ones((15,80))
h, w = img.shape[:2]
print h,w
small_kernel = np.zeros((h+2, w+2), np.uint8) 

#  image - image opening with kernel 


img = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)

ret,img = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

threshold_img = img.copy()

## inverted image



cv2.floodFill(img,small_kernel,(0,0),255)
img = cv2.bitwise_not(img)
img = img | threshold_img

img = cv2.morphologyEx(img,cv2.MORPH_OPEN,big_kernel)

#plt.imshow(img, cmap ='gray')
#plt.show()


'''
yMax = np.where(img==img.max())[1].max()
yMin = np.where(img==img.max())[1].min()
xMax = np.where(img==img.max())[0].max()
xMin = np.where(img==img.max())[0].min()

d_x = np.where(img[:,yMax]==img[:,yMax].max())[0].max()
slope = float(d_x - xMin) / (yMax - yMin)
theta = math.atan(slope)
'''



centre_x = np.where(img==img.max())[0].mean()
centre_y = np.where(img==img.max())[1].mean()
length = 125
height = 35
numbers = org_img[centre_x - height/2:centre_x + height/2,centre_y - length/2:centre_y + length/2]

#plt.imshow(numbers, cmap ='gray')
#plt.show()


############################## character segmentation 

numbers = cv2.dilate(numbers,np.ones((1,1)),iterations=1)
numbers = cv2.bitwise_not(numbers)

ret,numbers = cv2.threshold(numbers,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
numbers_copy = numbers.copy()
contours,heirachy = cv2.findContours(numbers,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


rects = [ cv2.boundingRect(c) for c in contours if cv2.contourArea(c) >= 10 ]

#numbers_copy = cv2.GaussianBlur(numbers_copy,(3,3),0)
rects.sort()
for rect in rects:
	x,y,w,h = rect

	character = numbers_copy[y-2:y+h+2,x-2:x+w+2]

	scale_x = 32.0/(w+4)
	scale_y = 32.0/(h+4)

	character = cv2.resize(character, (0,0), fx = 32.0/(w+4), fy= 32.0/(h+4))
	

	plt.imshow(character, cmap ='gray')
	plt.show()
	

# Show keypoints







