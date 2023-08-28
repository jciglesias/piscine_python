import pandas as pd

class SpatioTemporalData:
    def __init__(self, data: pd.DataFrame) -> None:
        self.data = data
    
    def when(self, location) -> list:
        """
        Takes a location as an argument and returns a list containing the
        years where games were held in the given location
        """
        return list({self.data["Year"][x] for x in range(len(self.data)) if self.data["City"][x] == location})

    def where(self, date) -> list:
        """
        Takes a date as an argument and returns the location where the
        Olympics took place in the given year.
        """
        return list({self.data["City"][x] for x in range(len(self.data)) if self.data["Year"][x] == date})