from matplotlib.pyplot import show, plot
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
import copy
import time

method = sys.argv[1:][0]


if(method == 'edgeDetect'):
	print "Detecting edges"
	img = mpimg.imread('../pictures/cycle.jpg')
	#Conversion to greyscale
	(m,n,o) = img.shape
	newImg = numpy.zeros((m,n))
	
	for i in range(m):
		for j in range(n):
			newImg[i][j] = numpy.average(img[i][j])

		
	img = copy.copy(newImg)

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

	f = open('data.pkl','rb')
	finalImg = pickle.load(f)
	f.close()



	(m,n) = finalImg.shape



	xSample = 0
	ySample = 0



	while(xSample < m and ySample < n):
		im = Image.new('RGB',(m,n))	
		x = random.sample(range(1,m),xSample)
		y = random.sample(range(1,n),ySample)

		for i in range(xSample):
			for j in range(ySample):
				value = int(finalImg[x[i]][y[j]])
				#value = int(newImg[i][j])
				im.putpixel((m-1-x[i],y[j]),(value,value,value))

		im = ndimage.rotate(im,90)
		fig = plt.figure()
		
		plt.imshow(im,cmap = plt.get_cmap('gray'))
		plt.show(block=False)
		time.sleep(1)
		plt.close()
		xSample += 5
		ySample += 5

	plt.imshow(finalImg,cmap = plt.get_cmap('gray'))
	plt.show()		








