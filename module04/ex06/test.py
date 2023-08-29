from FileLoader import FileLoader
from MyPlotLib import MyPlotLib as mpl

if __name__=="__main__":
    loader = FileLoader()
    data = loader.load('data/athlete_events.csv')

    mpl.histogram(data, ["Height", "Weight"])
    mpl.density(data, ["Height", "Weight"])
    mpl.pair_plot(data, ["Height", "Weight"])
    mpl.box_plot(data, ["Height", "Weight"])
