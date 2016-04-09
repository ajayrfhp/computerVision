from imports import *

img = cv2.imread('../pictures/coins_2.jpg')


dummy = img.copy()
dummy = cv2.cvtColor(dummy,cv2.COLOR_BGR2RGB)



img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 11, 1)

plt.imshow(img, cmap = 'gray' )
plt.show()



contours, heirachy = cv2.findContours(img.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = 0
for c in contours:
	area  = cv2.contourArea(c)
	if ( area <= 120000 or area >= 350000 ):
		continue
	if( len(c) < 5 ):
		continue
	(x,y),r = cv2.minEnclosingCircle(c)
	cv2.circle(dummy,(int(x),int(y)),int(r),(0,255,255),2)
	cnt += 1
print cnt 	 

plt.imshow(dummy)
plt.show()






 