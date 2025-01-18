
import numpy as np

def dice_score(y_true, y_pred):
	# Write your code here
	intersection = np.logical_and(y_pred,y_true).sum()
	t_sum = y_true.sum()
	p_sum = y_pred.sum()
	if t_sum==0 or p_sum==0:
		return 0.0
	else:	
		dice = 2 * intersection / (t_sum + p_sum)
		return round(dice, 3)

y_true = np.array([1, 1, 0, 0]) 
y_pred = np.array([0, 0, 1, 1]) 
print(dice_score(y_true, y_pred))