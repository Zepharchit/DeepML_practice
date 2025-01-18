import numpy as np 
def pca(data: np.ndarray, k: int) -> np.ndarray:

    # step to find pca 

    #1. standardise the data 
    data = (data - np.mean(data,axis=0)) / (np.std(data,axis=0))
    #2. covariance matrix
    cov = np.cov(data,rowvar=False)
    #3. get eigen values & vectors
    eig_val,eig_vec = np.linalg.eig(cov)
    
    #4. Sort the eigenvectors by decreasing eigenvalue
    idx = np.argsort(eig_val)[::-1]
    eig_vec = eig_vec[:,idx]
    #5. top k eigen vectors
    pca = eig_vec[:,:k]

    return np.round(pca,4) 

print(pca(np.array([[1, 2], [3, 4], [5, 6]]), k = 1))