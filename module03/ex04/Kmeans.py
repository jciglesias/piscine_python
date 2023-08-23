import sys, csv

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

if __name__=="__main__":
    if len(sys.argv[1:]) == 3:
        arg = [splt.split("=") for splt in sys.argv[1:]]
        arg = { k:v for [k,v] in arg}
        kmeans = KmeansClustering(arg["max_iter"], arg["ncentroid"])
        try:
            with open(arg["filepath"]) as csvfile:
                reader = list(csv.DictReader(csvfile))
        except Exception as e:
            print(e)
    else:
        print("Usage:  python3 Kmeans filepath='PATH' ncentroid=4 max_iter=30")