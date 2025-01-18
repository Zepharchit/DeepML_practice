import numpy as np

def f_score(y_true, y_pred, beta):
	"""
	Calculate F-Score for a binary classification task.

	:param y_true: Numpy array of true labels
	:param y_pred: Numpy array of predicted labels
	:param beta: The weight of precision in the harmonic mean
	:return: F-Score rounded to three decimal places
	"""
	tp = np.sum((y_true==1) & (y_pred==1))
	fn = np.sum((y_true==1) & (y_pred==0))
	fp = np.sum((y_true==0) & (y_pred==1))

	if tp + fp ==0 or tp + fn==0:
		return 0
	p = tp / (tp + fp)
	r = tp / (tp + fn)

	return round((1 + beta**2) * (p * r) / ((beta**2 * p)+r),3)

y_true = np.array([1, 0, 1, 1, 0, 1]) 
y_pred = np.array([1, 0, 1, 0, 0, 1]) 
beta = 1 
y_true=np.array([1, 0, 1, 1, 0]), np.array([1, 0, 0, 1, 1])
print(f_score(y_true, y_pred, beta))