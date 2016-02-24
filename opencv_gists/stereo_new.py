from imports import *
import scipy
from skimage.feature import match_template

def isvalid(i,j,r,c):
	return ( i>=0 and j>=0 and i<r and j<c )

def template_match(img,tempate):
	'''
		slice all subimages from image, find one with minimum deviation from the template
	'''

	num_slices = img.shape[1] / tempate.shape[1]
	rt,ct = tempate.shape
	min_deviation_so_far = sys.maxint
	answer = -1
	for i in range(num_slices):
		img_slice = img[:,i*ct:(i+1)*ct]
		this_deviation = np.linalg.norm(tempate - img_slice)
		if( this_deviation < min_deviation_so_far ):
			min_deviation_so_far = this_deviation 
			answer = i*ct

	return answer



def disparity_map(left,right,window,thresh):
	rows,columns = left.shape
	dmp = np.zeros((rows,columns))
	
	'''
		break down image row by row.
		each row, break into tempates ( size window * window ).
		feed into template matching function that row and that template,
		disparity value for all values withing that template is determined from template_match function
	'''

	num_row_slices = left.shape[0] / window
	num_col_slices = left.shape[1] / window
	
	ri,ci = left.shape
	
	for i in range(num_row_slices):
		left_row_slice = left[i*window:(i+1)*window,]
		for j in range(num_col_slices):


			left_template = left_row_slice[:,j*window:(j+1)*window]
			right_row_slice = right[i*window:(i+1)*window,max(0,j*window-thresh):min(ci,j*window+thresh)]		
		
			x = template_match(right_row_slice,left_template)
			#corr = match_template(right_row_slice,left_template)
			#x,y = np.unravel_index(np.argmax(corr), corr.shape)[::-1]
			#print x,y


			disparity = abs(j*window - x)
			dmp[ri-1-(i*window),j*window] = disparity


			'''
			for k in range(window):
				for l in range(window):
					dmp[ ri -1 - (i*window+k),j*window+l] = disparity
			'''

	dmp = gaussian_filter(dmp,sigma = 20)

	dmp = np.transpose(dmp)
	dmp = abs(dmp - dmp.max())
			
				
	return dmp


img_left = cv2.imread('../pictures/l.png')
img_right = cv2.imread('../pictures/r.png')


left = img_left.copy()
right = img_right.copy()
img_left = cv2.cvtColor(img_left,cv2.COLOR_BGR2GRAY)
img_right = cv2.cvtColor(img_right,cv2.COLOR_BGR2GRAY)
img_left = img_left 
img_right = img_right

stereo = cv2.StereoBM(1,16,11)
disparity = stereo.compute(img_left,img_right)
dmp = disparity_map(img_left,img_right,11,100) 


plt.imshow(dmp,cmap = 'gray')
plt.show()


