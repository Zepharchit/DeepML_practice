import numpy as np
def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	a = np.array(a)
	b = np.array(b)
	ca = np.shape(a)[1]
	rb = np.shape(b)[0]
	if ca!=rb:
		return -1
	
	return np.dot(a,b)

print(matrix_dot_vector([[1,2,3],[2,4,5],[6,8,9]],[1,2,3]))
print(matrix_dot_vector([[1,2],[2,4],[6,8],[12,4]],[1,2,3]))
print(matrix_dot_vector([[1, 2, 3], [2, 4, 6]],[1, 2, 3]))