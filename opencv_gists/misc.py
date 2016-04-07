from imports import *

img = cv2.imread('../pictures/ajay.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_x_derivative = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
img_y_derivative = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
img_w_xx = scipy.ndimage.filters.gaussian_filter(img_x_derivative*img_x_derivative,1)
plt.imshow(img_w_xx,cmap = 'gray')
plt.show()
