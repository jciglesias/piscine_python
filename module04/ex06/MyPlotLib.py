from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

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
        for x in features:
            sns.kdeplot(data[x])
        plt.legend(features)
        plt.show()
    def pair_plot(data: pd.DataFrame, features: list): 
        """
        Plots a matrix of subplots (also called scatter plot matrix).
        On each subplot shows a scatter plot of one numerical variable
        against another one. The main diagonal of this matrix shows
        simple histograms.
        """
        if len(features) == 2:
            fig, ax = plt.subplots(2, 2,  tight_layout=True)
            ax[0][0].hist(data[features[0]])
            ax[0][0].legend([features[0]])
            ax[0][0].grid(visible=True, which="both", axis="both")
            ax[0][1].scatter(data[features[0]], data[features[1]])
            ax[1][0].scatter(data[features[1]], data[features[0]])
            ax[1][1].hist(data[features[1]])
            ax[1][1].legend([features[1]])
            ax[1][1].grid(visible=True, which="both", axis="both")
            plt.show()
    def box_plot(data: pd.DataFrame, features: list): 
        """
        Displays a box plot for each numerical variable in the dataset.
        """
        fig, ax = plt.subplots(1,len(features))
        for x in range(len(features)):
            ax[x].boxplot([i for i in data[features[x]] if ~np.isnan(i)])
            ax[x].set_title(features[x])
        plt.show()
    pass
