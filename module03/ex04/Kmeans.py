import sys, csv
import numpy as np

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids
    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        -----
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
            None.
        Raises:
        -------
            This function should not raise any Exception.
        """
        if isinstance(X, np.ndarray):
            data = X.copy()

            # Calculate ncentroids percentiles
            p = 100 / (self.ncentroid + 1)
            for i in range(1, self.ncentroid + 1):
                self.centroids.append(list(np.percentile(data, p * i, axis=0)))
            self.centroids = np.array(self.centroids)

            # Or do it random:
            # self.centroids = data[np.random.choice(data.shape[0], self.ncentroid, replace=False)]

            for i in range(self.max_iter):
                # Calculate distances between data points and centroids
                distances = np.sqrt(((data[:, np.newaxis, :] - self.centroids) ** 2).sum(axis=2))

                # Assign each data point to the closest centroid
                labels = np.argmin(distances, axis=1)

                # Update centroids as the mean of data points in each cluster
                new_centroids = np.array([data[labels == k].mean(axis=0) for k in range(self.ncentroid)])

                # Check for convergence
                print(i)
                if np.all(self.centroids == new_centroids):
                    break
                
                self.centroids = new_centroids
        return None

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
            the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
            This function should not raise any Exception.
        """
        if isinstance(X, np.ndarray):
            distances = np.sqrt(((X[:, np.newaxis, :] - self.centroids) ** 2).sum(axis=2))
            return(np.argmin(distances, axis=1))
        return None

if __name__=="__main__":
    if len(sys.argv[1:]) == 3:
        arg = [splt.split("=") for splt in sys.argv[1:]]
        arg = { k:v for [k,v] in arg}
        kmeans = KmeansClustering(int(arg["max_iter"]), int(arg["ncentroid"]))
        try:
            with open(arg["filepath"]) as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                data = np.array([[float(x) for x in row[1:]] for row in reader])
            kmeans.fit(data)
            print(kmeans.predict(data))
        except Exception as e:
            print(e)
    else:
        print("Usage:  python3 Kmeans filepath='PATH' ncentroid=4 max_iter=30")