import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy
from numpy import *
from skimage import color
from convolution import *
from scipy import ndimage



img = color.rgb2gray(mpimg.imread('../pictures/ajay.jpg'))

mask = numpy.array([[-1,0,1],[-2,0,2],[-1,0,1]])

img2 = convolve(img,mask) 



plt.imshow(img2,cmap = plt.get_cmap('gray'))
plt.show()




