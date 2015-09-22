import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy
from numpy import *
from skimage import color
from convolution import *
import pickle
import sys

method = sys.argv[1:]
print method[0]

if(method[0] == 'edgeDetect'):
	print "Detecting edges"
	img = color.rgb2gray(mpimg.imread('../pictures/cycle.jpg'))
	maskx = numpy.array([[-1,0,1],[-2,0,2],[-1,0,1]])
	masky = numpy.transpose(maskx)
	img2 = convolve(img,maskx) 
	img3 = convolve(img,masky)
	finalImg = numpy.hypot(img2,img3)
	
	f = open('data.pkl','wb')
	pickle.dump(finalImg,f)
	f.close()
	print "dumping data"

	plt.imshow(finalImg,cmap = plt.get_cmap('gray'))
	plt.show()



elif(method[0] == 'load'):
	print "loading data"
	f = open('data.pkl','rb')
	finalImg = pickle.load(f)
	f.close()
	print "drawing image"
	plt.imshow(finalImg,cmap = plt.get_cmap('gray'))
	plt.show()



