def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
	a,b,c,d = matrix[0][0],matrix[0][1],matrix[1][0],matrix[1][1]
	det = a*d - c*b
	if det == 0:
		return None
	
	return [[d/det,-b/det],[-c/det,a/det]]
print(inverse_2x2([[4, 7], [2, 6]]))