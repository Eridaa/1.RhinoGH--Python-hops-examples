import numpy as np
import rhino3dm
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

def numpyToPoints(X):
    rhino_points = []
    for n in X:
        p = rhino3dm.Point3d(n[0], n[1], 0)
        rhino_points.append(p)
    return rhino_points

def kmeans(n):

    X, y_true = make_blobs(n_samples=300, centers=4,
                        cluster_std=0.60, random_state=0)


    #peform kmeans clustering
    kmeans = KMeans(n)
    res = kmeans.fit_predict(X)
    clusters = res.tolist()

    #convert clusters to string
    string_clusters = []
    for c in clusters:
        str_cluster = str(c)
        string_clusters.append(str_cluster)

    points = numpyToPoints(X)
    print (points)
    return points, clusters

kmeans(5)


