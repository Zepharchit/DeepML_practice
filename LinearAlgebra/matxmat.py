def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	if len(a[0])!=len(b):
		return -1
	
	res = []
	for r in range(len(a)):
		tmp = []
		for c in range(len(b[0])):
			val = 0
			for k in range(len(b)):
				val+=a[r][k] * b[k][c]
			tmp.append(val)
		res.append(tmp)
	return res

print(matrixmul([[1,2,3],[2,3,4],[5,6,7]],[[3,2,1],[4,3,2],[5,4,3]]))