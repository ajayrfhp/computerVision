from imports import *

img = cv2.imread('../pictures/car.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
f_img = np.fft.fft2(img)
f_img = np.fft.fftshift(f_img)
magnitude_img = np.log(abs(f_img))




blurred_img = np.zeros(f_img.shape,dtype = 'complex')
blurred_img[150:200,260:320] = f_img[150:200,260:320]

if_blur_img = np.fft.ifftshift(blurred_img)
if_blur_img = np.fft.ifft2(if_blur_img)
if_blur_img = abs(if_blur_img)


filtered_img = f_img
filtered_img[150:200,260:320] = 0

if_filter_img = np.fft.ifftshift(filtered_img)
if_filter_img = np.fft.ifft2(if_filter_img)
if_filter_img = abs(if_filter_img)




plt.imshow(if_blur_img, cmap = 'gray')
plt.show()
plt.imshow(if_filter_img, cmap = 'gray')
plt.show()