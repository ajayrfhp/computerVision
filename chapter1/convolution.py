import numpy 
from numpy import *


def convolve(a,mask):
	mA = a.shape[0]
	nA = a.shape[1] 

	mMask = mask.shape[0]
	nMask = mask.shape[1] 
	# store dimensions

	c = numpy.zeros((mA,nA))
	mask = numpy.fliplr(mask)
	mask = numpy.flipud(mask)
	for i in range(mA):
		for j in range(nA):
			# determine coordinates for translation of the mask
			ti = (mMask)/2- i
			tj = (nMask)/2 - j

			for i2 in range(mA):
				for j2 in range(nA):
					if(i2 + ti < mMask and j2 + tj < nMask and i2+ti>=0 and j2+tj>=0):
						c[i][j] += a[i2][j2] * mask[i2+ti][j2+tj]

			#print str(i) + ',' + str(j)
			#print str(ti) + ',' + str(tj)
			#print '-------------'
		
	return c

#a = numpy.array([[2,4,6],[8,10,12],[14,16,18]])
#mask = numpy.array([[9,8,7],[6,5,4],[3,2,1]])

#a = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
#mask = numpy.array([[-1,-2,-1],[0,0,0],[1,2,1]])

a = numpy.array([[1,5,2,3],[8,7,3,6],[3,3,9,1]])
mask = numpy.array([[1,2,3],[0,0,0],[6,5,4]])

print convolve(a,mask)
