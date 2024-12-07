import numpy as np

def make_diagonal(x):
	# Your code here
	mat = np.diag(x)
	return mat
print(make_diagonal(np.array([1, 2, 3])))
print(make_diagonal(np.array([4, 5, 6, 7])))