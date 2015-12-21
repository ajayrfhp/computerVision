from imports import *

img = cv2.imread('../pictures/car.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


plt.hist(img.flatten(),256,[0,256],color = 'r')
plt.show()
img = cv2.equalizeHist(img)
plt.hist(img.flatten(),256,[0,256],color = 'r')
plt.show()
#plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))

plt.imshow(img, cmap = 'gray')
plt.show()
