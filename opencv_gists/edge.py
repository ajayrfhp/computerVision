import numpy as np 
from matplotlib import pyplot as plt 
import cv2

img = cv2.imread('../pictures/ps1_1.png')
edge_img = cv2.Canny(img,0,1)
plt.imshow(edge_img, cmap = 'gray')
plt.show()