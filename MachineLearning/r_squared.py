
import numpy as np

def rmse(y_true, y_pred):
	# Write your code here
	if y_true.shape!=y_pred.shape:
		raise ValueError("Array should be of same size")
	if y_true.size==0:
		raise ValueError("Array cannot be empty")
	summed_diff = np.mean((y_true - y_pred)**2)
	rmse_res = np.sqrt(summed_diff)
	return round(rmse_res,3)

import numpy as np

def r_squared(y_true, y_pred):
	# Write your code here
	ssr = np.sum((y_true - y_pred)**2)
	sst = np.sum((y_true - np.mean(y_true))**2)
	r2 = 1 - (ssr/sst)
	return r2
y_true = np.array([1, 2, 3, 4, 5]) 
y_pred = np.array([1, 2, 3, 4, 5]) 
print(r_squared(y_true, y_pred))