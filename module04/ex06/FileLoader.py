import pandas as pd

class FileLoader:
    def load(self, path):
        """
        takes as an argument the file path of the dataset to load,
        displays a message specifying the dimensions of the dataset (e.g. 340 x 500) and
        returns the dataset loaded as a pandas.DataFrame.
        """
        try:
            data = pd.read_csv(path)
            print(data.shape)
            return data
        except Exception as e:
            print(e)
    def display(self, df:pd.DataFrame, n):
        """
        takes a pandas.DataFrame and an integer as arguments,
        displays the first n rows of the dataset if n is positive,
        or the last n rows if n is negative.
        """
        try:
            if n >= 0:
                print(df.loc[[i for i in range(n)]])
            else:
                size = len(df)
                print(df.loc[[i for i in range(size + n, size)]])
        except Exception as e:
            print(e)