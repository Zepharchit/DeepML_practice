import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	correct = y_pred[y_pred==y_true]
	return len(correct) / len(y_true)

def precision(y_true, y_pred):
	# Your code here
	tp = np.sum((y_true==1) & (y_pred==1))
	fp = np.sum((y_true==0) & (y_pred==1))
	return tp / (tp + fp) if (tp + fp) >0 else 0


y_true = np.array([1, 0, 1, 1, 0, 1]) 
y_pred = np.array([1, 0, 1, 0, 0, 1]) 
result_acc = accuracy_score(y_true, y_pred)
result_pre = precision(y_true,y_pred) 
print(result_acc)
print(result_pre)