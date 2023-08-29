from matplotlib import pyplot as plt
import pandas as pd

class MyPlotLib:
    def histogram(data: pd.DataFrame, features: list):
        """
        Plots one histogram for each numerical feature in
        the list
        """
        try:
            fig, ax = plt.subplots(1, len(features),  tight_layout=True)
            for x in range(len(features)):
                ax[x].hist(data[features[x]])
                # histtype: Literal['bar', 'barstacked', 'step', 'stepfilled']
                ax[x].legend([features[x]])
                ax[x].grid(visible=True, which="both", axis="both")
            plt.show()
        except Exception as e:
            print(e)
    def density(data: pd.DataFrame, features: list): 
        """
        plots the density curve of each numerical feature in
        the list
        """
        # for x in features:
        #     plt.scatter(data[x])
    def pair_plot(data: pd.DataFrame, features: list): 
        """
        Plots a matrix of subplots (also called scatter plot matrix).
        On each subplot shows a scatter plot of one numerical variable
        against another one. The main diagonal of this matrix shows
        simple histograms.
        """
        pass
    def box_plot(data: pd.DataFrame, features: list): 
        """
        Displays a box plot for each numerical variable in the dataset.
        """
        pass
    pass
