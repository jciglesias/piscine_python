import pandas as pd

class Komparator:
    def compare_box_plots(self, categorical_var, numerical_var):
        """
        displays a series of box plots to compare how the distribution
        of the numerical variable changes if we only consider the
        subpopulation which belongs to each category. There should
        be as many box plots as categories. For example, with Sex and
        Height, we would compare the height distributions of men vs.
        women with two box plots.
        """
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