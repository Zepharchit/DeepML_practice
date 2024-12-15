import numpy as np 

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	A = np.array(A)
	T = np.array(T)
	S = np.array(S)
	if not np.linalg.det(T) or not np.linalg.det(S):
		return -1
	t_inv = np.linalg.inv(T) 
	int_1 = np.dot(t_inv,A)
	transformed_matrix =  np.dot(int_1,S)
	return transformed_matrix.tolist()

print(transform_matrix([[1, 2], [3, 4]], [[2, 0], [0, 2]], [[1, 1], [0, 1]]))