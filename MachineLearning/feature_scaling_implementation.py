import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	
	mean = np.mean(data,axis=0)
	std = np.std(data,axis=0)
	standardized_data = (data - mean) / (std)

	maxed = np.max(data,axis=0)
	mined = np.min(data,axis=0)
	normalized = ((data - mined)/(maxed - mined)) 
	return standardized_data, normalized