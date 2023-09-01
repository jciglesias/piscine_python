from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

class Komparator:
    def __init__(self, data: pd.DataFrame) -> None:
        self.data = data
    def compare_box_plots(self, categorical_var:str, numerical_var:str):
        """
        displays a series of box plots to compare how the distribution
        of the numerical variable changes if we only consider the
        subpopulation which belongs to each category. There should
        be as many box plots as categories. For example, with Sex and
        Height, we would compare the height distributions of men vs.
        women with two box plots.
        """
        cat = self.data[categorical_var]
        num = self.data[numerical_var]
        x = list({i for i in cat if i is not np.nan})
        fig, ax = plt.subplots(1,len(x))
        for i in range(len(x)):
            ax[i].plot(num)
        plt.show()

    def density(self, categorical_var, numerical_var):
        """
        displays the density of the numerical variable. Each
        subpopulation should be represented by a separate curve
        on the graph.
        """
    def compare_histograms(self, categorical_var, numerical_var):
        """
        plots the numerical variable in a separate histogram
        for each category. As an extra, you can use overlapping
        histograms with a color code.
        """