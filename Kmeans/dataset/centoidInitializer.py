import numpy as np
X = np.loadtxt('C:/Users/david/Documents/Masters/COMP41110_Cloud_Computing/Project/Kmeans/MapReduce/dataset.txt',delimiter=',')
from sklearn.cluster import KMeans
km = KMeans(n_clusters=2,n_init = 1, max_iter =1,random_state=1)

m = km.fit(X)
centroids = km.cluster_centers_
np.savetxt('C:/Users/david/Documents/Masters/COMP41110_Cloud_Computing/Project/Kmeans/MapReduce/centroids.txt',centroids,delimiter = ',',fmt='%f')

