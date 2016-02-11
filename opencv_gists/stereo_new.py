from imports import *

def isvalid(i,j,r,c):
	return ( i>=0 and j>=0 and i<r and j<c )


def disparity_map(left,right,window,thresh):
	rows,columns = left.shape
	dmp = np.zeros((rows,columns))
	
	for h in range(0,rows):
		for i in range(0,columns,window):
			if( not isvalid((h+window),(i+window),rows,columns) ):
				break
			answer = -1
			min_deviation = sys.maxint
			sample_left = left[h:h+window,i:i+window]
			for j in range(i-thresh,i+thresh,window):
				if( not isvalid(0,j+window,rows,columns) or  not isvalid(0,j,rows,columns) ):
					break
				sample_right = right[h:h+window,j:j+window]
				deviation = np.linalg.norm(sample_left - sample_right)
				if(deviation < min_deviation ):
					min_deviation = deviation
					answer = abs( i - j)
			

			for j in range(h,h+window):
				for k in range(i,i+window):
					dmp[j,k] = answer 		


	
		



	return dmp






img_left = cv2.imread('../pictures/left.png')
img_right = cv2.imread('../pictures/right.png')


left = img_left.copy()
right = img_right.copy()
img_left = cv2.cvtColor(img_left,cv2.COLOR_BGR2GRAY)
img_right = cv2.cvtColor(img_right,cv2.COLOR_BGR2GRAY)
img_left = img_left *1.0 / 255.0
img_right = img_right * 1.0 / 255.0


dmp = disparity_map(img_left,img_right,10,50) 
z = dmp[:-10,:-10]


plt.imshow(img_left,cmap = 'gray')
plt.show()
plt.pcolor(z)
plt.show()


