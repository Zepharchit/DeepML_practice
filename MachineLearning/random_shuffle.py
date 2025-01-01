import numpy as np

def shuffle_data(X, y, seed=None):
	# Your code here
	if seed:
		np.random.seed(seed)
	index = np.random.permutation(len(X))
	return X[index],y[index]

print(shuffle_data(np.array([[1, 2], 
                  [3, 4], 
                  [5, 6], 
                  [7, 8]]),np.array([1, 2, 3, 4])))