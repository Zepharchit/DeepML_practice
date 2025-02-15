import numpy as np
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
	# Your code here, make sure to round
	m, n = X.shape
	theta = np.zeros((n, 1)) # weight init
	for _ in range(iterations):
		preds = X @ theta
		error = preds - y.reshape(-1,1)
		update = X.T @ error / m
		theta -= alpha * update
	return theta

print(linear_regression_gradient_descent(np.array([[1, 1], [1, 2], [1, 3]]), np.array([1, 2, 3]), 0.01, 1000))