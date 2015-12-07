import numpy as np 
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('../pictures/ajay.jpg')
kernel = np.ones((5,5))/25

filtered_img = cv2.filter2D(img,-1,kernel)

plt.imshow(filtered_img,cmap = 'gray')
plt.show()



