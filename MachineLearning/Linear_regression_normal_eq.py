import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	X = np.array(X)
	y = np.array(y)
	prod = X.T @ y
	inv_comp = np.linalg.inv(X.T @ X)
	theta = inv_comp @ prod
	return theta

print(linear_regression_normal_equation([[1, 1], [1, 2], [1, 3]], [1, 2, 3]))
print(linear_regression_normal_equation([[1, 3, 4], [1, 2, 5], [1, 3, 2]], [1, 2, 1]))
