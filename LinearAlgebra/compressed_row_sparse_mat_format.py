import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

	:param dense_matrix: 2D list representing a dense matrix
	:return: A tuple containing (values array, column indices array, row pointer array)
	"""
	mat = np.array(dense_matrix)
	values = mat[mat!=0]
	_,col_ids = np.nonzero(mat)
	rpa = [0]
	init_val = 0
	for row in mat:
		init_val+=len(row[row!=0])
		rpa.append(init_val)
	return (values.tolist(),col_ids.tolist(),rpa)

dense_matrix = [
    [1, 0, 0, 0],
    [0, 2, 0, 0],
    [3, 0, 4, 0],
    [1, 0, 0, 5]
]
vals, col_idx, row_ptr = compressed_row_sparse_matrix(dense_matrix)
print("Values array:", vals)
print("Column indices array:", col_idx)
print("Row pointer array:", row_ptr)