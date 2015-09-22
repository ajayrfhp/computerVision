import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy
from numpy import *
from skimage import color
from convolution import *
from scipy import ndimage



img = color.rgb2gray(mpimg.imread('../pictures/ajay.jpg'))

maskx = numpy.array([[-1,0,1],[-2,0,2],[-1,0,1]])
masky = numpy.transpose(maskx)
img2 = convolve(img,maskx) 
img3 = convolve(img,masky)

finalImg = numpy.hypot(img2,img3)


plt.imshow(finalImg,cmap = plt.get_cmap('gray'))
plt.show()





