import pandas as pd
import numpy as np

def youngest_fellah(data: pd.DataFrame, year: int) -> dict:
    # [RangeIndex(start=0, stop=271116, step=1),
    # Index(['ID', 'Name', 'Sex', 'Age', 'Height', 'Weight', 'Team', 'NOC', 'Games', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal'], dtype='object')]
    try:
        females = []
        males = []
        for x in range(len(data)):
            if data["Year"][x] == year:
                if data["Sex"][x] == "F":
                    females.append(data["Age"][x])
                elif data["Sex"][x] == "M":
                    males.append(data["Age"][x])
        rf = np.nan if not females else np.nanmin(females)
        rm = np.nan if not males else np.nanmin(males)
        return {"f": rf, "m": rm}
        

    except Exception as e:
        print(e)