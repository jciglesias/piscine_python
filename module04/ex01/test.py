from FileLoader import FileLoader
from YoungestFellah import youngest_fellah

loader = FileLoader()
data = loader.load("data/athlete_events.csv")
# Output
# (271116, 15) 
print("Example 1:")
print(youngest_fellah(data, 2004))
# Output
# {’f’: 13.0, ’m’: 14.0}