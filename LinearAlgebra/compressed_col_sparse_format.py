import numpy as np
def compressed_col_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix into its Compressed Column Sparse (CSC) representation.

	:param dense_matrix: List of lists representing the dense matrix
	:return: Tuple of (values, row indices, column pointer)
	"""
	mat = np.array(dense_matrix)
	row_ids,_ = np.nonzero(mat)
	mat = mat.T
	values = mat[mat!=0]
	cpa = [0]
	init_val = 0
	for col in mat:
		init_val += len(col[col!=0])
		cpa.append(init_val)
	values = values.tolist()
	row_ids = row_ids.tolist()
	return values,row_ids,cpa
	
