from imports import *

def is_in_bounds(x,l,u):
	return x >= l and x < u

'''
	Note, we need to obtain one score for each and every pixel. We can obtain that by operating on image level itself, there is no need to compute score pixel wise. No loops.
	M = [ Wxx Wxy  
	      Wxy Wyy ]
	Score = det(M) / trace (M)      

'''

img = cv2.imread('../pictures/chess_board.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
epsilon = 10**(-4)
img_x_derivative = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
img_y_derivative = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
img_w_xx = scipy.ndimage.filters.gaussian_filter(img_x_derivative*img_x_derivative,1)
img_w_yy= scipy.ndimage.filters.gaussian_filter(img_y_derivative*img_y_derivative,1)
img_w_xy = scipy.ndimage.filters.gaussian_filter(img_x_derivative*img_y_derivative,1)
det_m = img_w_xx * img_w_yy - (img_w_xy)**2
trace_m = img_w_xx + img_w_yy
scores = det_m / (trace_m + epsilon)
scores[scores>=scores.mean()] = 1
scores[scores<scores.mean()] = 0
plt.imshow(scores,cmap = 'gray')
plt.show()



