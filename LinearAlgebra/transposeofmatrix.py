def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	b = []
	for i in range(len(a[0])):
		t = []
		for j in range(len(a)):
			t.append(a[j][i])
		b.append(t)
	return b

print(transpose_matrix([[1,2],[3,4],[5,6]]))
print(transpose_matrix([[1,2,3],[4,5,6]]))