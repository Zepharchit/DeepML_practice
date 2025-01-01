import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	# Your code here
	bs = batch_size
	res = []
	for i in range(0,len(X),bs):
		temp = []
		if y is not None:
			temp.append(X[i:i+bs,].tolist())
			temp.append(y[i:i+bs].tolist())
			res.append(temp)
		else:
			temp.append(X[i:i+bs,].tolist())
			res.append(temp)
	
	return res

print(batch_iterator(np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]), 
					 np.array([1, 2, 3, 4, 5]), batch_size=2))
