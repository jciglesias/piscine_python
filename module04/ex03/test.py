from FileLoader import FileLoader
from HowManyMedals import how_many_medals

loader = FileLoader()
data = loader.load("data/athlete_events.csv")
# Output
# Loading dataset of dimensions 271116 x 15
print(how_many_medals(data, "Kjetil Andr Aamodt"))
# Output
# {1992: {'G': 1, 'S': 0, 'B': 1},
# 1994: {'G': 0, 'S': 2, 'B': 1},
# 1998: {'G': 0, 'S': 0, 'B': 0},
# 2002: {'G': 2, 'S': 0, 'B': 0},
# 2006: {'G': 1, 'S': 0, 'B': 0}}
print(how_many_medals(data, 'Gary Abraham'))
#  the output is: 
# "{1976: {'G': 0, 'S': 0, 'B': 0}, 1980: {'G': 0, 'S': 0, 'B': 1}}"

print(how_many_medals(data, 'Yekaterina Konstantinovna Abramova'))
#  the output is 
# "{2006: {'G': 0, 'S': 0, 'B': 1}, 2010: {'G': 0, 'S': 0, 'B': 0}}"

print(how_many_medals(data, 'Kristin Otto'))
#  the output is: 
# "{1988: {'G': 6, 'S': 0, 'B': 0}}"