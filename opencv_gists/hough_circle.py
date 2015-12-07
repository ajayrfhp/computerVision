from imports import *

def hough(edges):
	h = np.zeros((1000,1000,15))
	for edge in edges:
		
		for r in range(1,15):
			for o in range(360):
				a =  round(edge[0] - r*np.cos(o*np.pi/180))
				b =  round(edge[1] - r*np.sin(o*np.pi/180))
	
				h[100+a,100+b,r] += 1
				

	a = np.where(h == h.max())[0][0] - 100
	b = np.where(h == h.max())[1][0] - 100
	r = np.where(h == h.max())[2][0]
	print a,b,r



def plot(edges):
	plt.plot(edges[:,0],edges[:,1],'o')
	plt.xlim([-5,5])
	plt.ylim([-5,5])
	plt.show()



'''
img = cv2.imread('../pictures/circle.jpg')
kernel = np.ones((2,2),np.float32) / 4
img = cv2.filter2D(img,-1,kernel)
edge_img = cv2.Canny(img,0,200,3)
plt.imshow(edge_img, cmap = 'gray')
plt.show()
'''

edges = np.array([[-3,0],[3,0],[0,-3],[0,3]])


hough(edges)
plot(edges)