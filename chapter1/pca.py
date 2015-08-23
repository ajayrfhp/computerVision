import numpy as np 
import matplotlib.pyplot as plt

X = np.array([[1,2],[3,4],[5,6]])

x = X - X.mean(axis=0)
cov = np.cov(np.transpose(x))
[u,s,v] = np.linalg.svd(cov)
u = u[0].reshape((u[0].shape[0],1))

print u

transformedX = np.dot(x,u)

plt.plot(x[:,0],x[:,1],'ro')
plt.axis([-6.0,6,-6,6.0])
plt.plot([0,u[0]],[0,u[1]])
plt.title('Principal Component Analysis. Unit vector')
plt.show()


print transformedX
	