def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode=='row':
		means = [sum(rows)/len(rows) for rows in matrix]
		return means
	else:
		means = [sum(col)/len(col) for col in zip(*matrix)]
		return means
print(calculate_matrix_mean([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 'column'))
print(calculate_matrix_mean([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 'row'))