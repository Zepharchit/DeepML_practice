import numpy as np
def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	# Your code here
	prediction = X @ w.T 
	diff = (y_true - prediction)**2
	mse = np.mean(diff)
	reg = alpha * np.sum(w**2)
	return mse + reg

X = np.array([[1,1],[2,1],[3,1],[4,1]]) 
W = np.array([.2,2]) 
y = np.array([2,3,4,5]) 
alpha = 0.1 
output = ridge_loss(X, W, y, alpha) 
print(output)