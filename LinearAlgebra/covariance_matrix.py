def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	n_feats = len(vectors)
	n_obs = len(vectors[0])
	means = [sum(feat)/len(feat) for feat in vectors]
	covariance_matrix = [[0 for _ in range(n_feats)] for _ in range(n_feats)]
	
	
	for i in range(n_feats):	
		for j in range(n_feats):
			covariance = sum((vectors[i][k] - means[i]) * (vectors[j][k] - means[j]) for k in range(n_obs)) / (n_obs - 1)
			covariance_matrix[i][j] = covariance_matrix[j][i] = covariance

	
	return covariance_matrix