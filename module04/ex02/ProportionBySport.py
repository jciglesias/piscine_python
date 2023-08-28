import pandas as pd

def proportion_by_sport(data: pd.DataFrame, year: int, sport: str, gender: str):
    sample = [data["Sport"][x] for x in range(len(data)) if data["Year"][x] == year and data["Sex"][x] == gender]
    total = len(sample)
    n_practices = len([x for x in sample if x == sport])
    return n_practices/total