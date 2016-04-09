import numpy as np 
from matplotlib import pyplot as plt 
import cv2,cv
from scipy import ndimage,signal
import scipy
import math
import time
import skimage
from skimage.feature import hog
from skimage import data, color, exposure
from sklearn.externals import joblib
import sys
from scipy.ndimage.filters import gaussian_filter
import pytesseract,Image
from sklearn import datasets, svm, metrics, preprocessing
from sklearn.cross_validation import train_test_split,cross_val_score
from sklearn.grid_search import GridSearchCV
import scipy

def convert(value):
	if(value <= 9):
		return value
	return chr(value - 10 + ord('a') ) 