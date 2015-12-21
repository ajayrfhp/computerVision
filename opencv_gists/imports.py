import numpy as np 
from matplotlib import pyplot as plt 
import cv2
from scipy import ndimage
import math
import time
from sklearn import svm
from sklearn.externals import joblib

def convert(value):
	if(value <= 9):
		return value
	return chr(value - 10 + ord('a') ) 