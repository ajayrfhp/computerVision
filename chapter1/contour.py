from PIL import Image
from pylab import *

img = array(Image.open('../pictures/0.png'))
print img.shape
print img[0][1]
figure()
imshow(img)
#gray()
#contour(img,origin='image')

show()