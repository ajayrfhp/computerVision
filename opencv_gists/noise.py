from imports import *

img = cv2.imread('../pictures/car.jpg')
img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)




filtered = cv2.GaussianBlur(img,(3,3),25)	

plt.imshow(filtered)
plt.show()