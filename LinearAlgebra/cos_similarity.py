import numpy as np

def cosine_similarity(v1, v2):
	# Implement your code here
	if len(v1)!=len(v2):
		return "Dimension Mismatch"
	numerator = np.dot(v1,v2)
	v1_norm = np.sqrt(np.sum(np.power(v1,2)))
	v2_norm = np.sqrt(np.sum(np.power(v2,2)))
	denom = v1_norm * v2_norm
	return round((numerator / denom),3)

v1 = np.array([1, 2, 3])
v2 = np.array([-1, -2, -3])
print(cosine_similarity(v1, v2))