from imports import *

def hough(edges):
	h = np.zeros((100,361))
	for edge in edges:
		for o in range(360):
			p = round(abs(edge[0]*np.cos(o*np.pi/180) + edge[1]*np.sin(o*np.pi/180)))
		
			h[p,o] += 1 
	return h,o,p

def plot(edges,h):
	h = h*255/h.max()  
	plt.imshow(h,cmap = 'gray')	
	plt.show()	


img = cv2.imread('../pictures/ps1_1.png')
edge_img = cv2.Canny(img,0,1)

h,o,p = hough(edge_img)
plot(edge_img,h)
