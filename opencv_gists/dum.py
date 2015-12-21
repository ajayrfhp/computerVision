from imports import *
img = cv2.imread('../pictures/T.png')
clf = joblib.load('../data/model.pkl')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,img = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
scale_x = 28.0/(img.shape[1])
scale_y = 28.0/(img.shape[0])

img = cv2.resize(img, (0,0), fx = scale_x, fy= scale_y)