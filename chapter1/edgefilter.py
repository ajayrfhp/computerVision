import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy
from numpy import *
from skimage import color
from convolution import *
import pickle
import sys
import Image
import random
from scipy import ndimage

method = sys.argv[1:][0]


if(method == 'edgeDetect'):
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



elif(method == 'load'):
	print "loading data"
	f = open('data.pkl','rb')
	finalImg = pickle.load(f)
	f.close()
	print "drawing image"	
	plt.imshow(finalImg,cmap = plt.get_cmap('gray'))
	plt.show()
	(m,n) = finalImg.shape
	finalImg[finalImg>0] = 255
	finalImg[finalImg<0] = 0


	im = Image.new('RGB', (m,n))
	x = random.sample(range(1,m),m-1)
	y = random.sample(range(1,n),n-1)
	for i in range(m):
		for j in range(n):
			value = int(finalImg[i][j])
			im.putpixel((i,j),(value,value,value))



	plt.imshow(im,cmap = plt.get_cmap('gray'))
	plt.show()


elif(method == 'test'):
	finalImg = mpimg.imread('../pictures/cycle.jpg')

	(m,n,o) = finalImg.shape
	newImg = numpy.zeros((m,n))
	
	for i in range(m):
		for j in range(n):
			newImg[i][j] = numpy.average(finalImg[i][j])

			
	

	im = Image.new('RGB', (m,n))



	for i in range(m):
		for j in range(n):
			x = int(newImg[i][j])
			im.putpixel((i,j),(x,x,x))

	im = ndimage.rotate(im,-90)


	plt.imshow(im)
	plt.show()









