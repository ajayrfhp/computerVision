from imports import *
img = cv2.imread('../pictures/red_threshold.jpg')
img = img[1:250,:,:]
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_r = img[:,:,0]
img_g = img[:,:,1]
img_b = img[:,:,2]
img_thresholded =cv2.subtract(img_r,cv2.add(img_g,img_b)) 



#ret,img_thresholded = cv2.threshold(img_thresholded,20,255,cv2.THRESH_BINARY)

plt.imshow(img_thresholded,cmap = 'gray')
plt.show()

'''

TODAY I LEARNT

img_g + img_b != cv2.add(img_g,img_b)

'''