from Komparator import Komparator as kp
from FileLoader import FileLoader as fl

floader = fl()
data = floader.load('data/athlete_events.csv')

com = kp(data) 
com.compare_box_plots("Medal", "Age")
com.compare_histograms("Medal", "Height")
com.density("Medal", "Weight")
