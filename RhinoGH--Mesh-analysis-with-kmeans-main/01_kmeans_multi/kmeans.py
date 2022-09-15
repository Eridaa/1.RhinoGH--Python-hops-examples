import numpy as np
from sklearn.cluster import KMeans

def kmeansAlgorithm(str_vec, n):

    vectors = []

    #deserialize this vectors
    for i in str_vec:
        vector = i.strip('][').split(',')
        vectors.append(vector)
    
    final_vectors = []
    for v in vectors:
        sub = []
        for c in v:
            fvector = float(c)
            sub.append(fvector)
        final_vectors.append(sub)

    
    #convert them to numpy arrays
    arr = np.array(final_vectors)


    #peform kmeans clustering
    kmeans = KMeans(n)
    res = kmeans.fit_predict(arr)
    clusters = res.tolist()

    #convert clusters to string
    string_clusters = []
    for c in clusters:
        str_cluster = str(c)
        string_clusters.append(str_cluster)

    return string_clusters
