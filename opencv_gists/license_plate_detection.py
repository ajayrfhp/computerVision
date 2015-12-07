from imports import *
img = cv2.imread('../pictures/car.jpg')
org_img = img.copy()
# convert to gray scale
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



# assumption is that we know size of the number plate, kernel size is to be changed depending upon that.
kernel = np.ones((10,10))
big_kernel = np.ones((15,80))
h, w = img.shape[:2]
print h,w
small_kernel = np.zeros((h+2, w+2), np.uint8) 

#  image - image opening with kernel 


img = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)



# adaptive

threshold = min(255,img.mean()*8)


ret,img = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
threshold_img = img.copy()



## inverted image

cv2.floodFill(img,small_kernel,(0,0),255)

img = cv2.bitwise_not(img)



img = img | threshold_img



img = cv2.morphologyEx(img,cv2.MORPH_OPEN,big_kernel)

plt.imshow(img, cmap ='gray')
plt.show()

centre_x = np.where(img==img.max())[0].mean()
centre_y = np.where(img==img.max())[1].mean()

length = 120
height = 35

number = org_img[centre_x - height/2:centre_x + height/2,centre_y - length/2:centre_y + length/2]


plt.imshow(number, cmap ='gray')
plt.show()
