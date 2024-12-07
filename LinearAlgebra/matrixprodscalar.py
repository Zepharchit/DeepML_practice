import numpy as np
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	#result = [scalar * matrix[i][j] for i in range(len(matrix))
	#		 for j in range(len(matrix[0]))]
	result = np.array(matrix) * scalar
	result = result.tolist()
	return result