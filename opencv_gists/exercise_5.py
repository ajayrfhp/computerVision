from imports import *

img1 = cv2.imread('../pictures/pic_1.jpg')
img2 = cv2.imread('../pictures/pic_2.jpg')



diff = abs(img1 - img2)
diff = cv2.cvtColor(diff,cv2.COLOR_BGR2RGB)


kernel = np.ones((3,3))

diff1 = cv2.erode(diff,kernel,0)
diff1 = cv2.dilate(diff1,kernel,0)


plt.imshow(diff1) 
plt.show()


diff2 = cv2.dilate(diff,kernel,0)
diff2 = cv2.erode(diff2,kernel,0)

plt.imshow(diff2) 
plt.show()