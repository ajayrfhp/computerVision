from imports import *


#img = color.rgb2gray(data.astronaut())


img = cv2.imread('../pictures/T.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img = cv2.Canny(img,100,200)






#features,img = skimage.feature.hog(img,orientations=3, pixels_per_cell=(3,3),cells_per_block=(1, 1),visualise = True ) 

img = np.array(img, dtype = np.uint8)


ret3,img = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)



plt.imshow(img, cmap = 'gray')
plt.show()