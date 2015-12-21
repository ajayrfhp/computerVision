from imports import *

start = time.time()

data = np.genfromtxt('../data/character.csv',delimiter=',') 

print time.time() - start