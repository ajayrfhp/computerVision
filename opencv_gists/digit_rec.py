from sklearn import datasets, svm, metrics
from sklearn.metrics import accuracy_score
import numpy as np
	
# The digits dataset
def digit_rec():
	digits = datasets.load_digits()
	n_samples = len(digits.images)
	data = digits.images.reshape((n_samples, -1))
	# Create a classifier: a support vector classifier
	classifier = svm.SVC(gamma=0.001)
	# We learn the digits on the first half of the digits
	classifier.fit(data[:n_samples / 2], digits.target[:n_samples / 2])
	expected = digits.target[n_samples / 2:]
	predicted = classifier.predict(data[n_samples / 2:])
	confusion_matrix = metrics.confusion_matrix(expected, predicted)

	print(np.mean(np.diag(confusion_matrix)))

	#req_inp = np.array([inp])
	#predicted_frm_inp = classifier.predict(req_inp)
	#return predicted_frm_inp

digit_rec()



