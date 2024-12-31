
import numpy as np

def rmse(y_true, y_pred):
	# Write your code here
	
	summed_diff = np.mean((y_true - y_pred)**2)
	rmse_res = np.sqrt(summed_diff)
	return round(rmse_res,3)
y_true1 = np.array([3, -0.5, 2, 7]) 
y_pred1 = np.array([2.5, 0.0, 2, 8]) 
print(rmse(y_true1, y_pred1))