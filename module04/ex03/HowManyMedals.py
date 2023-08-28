import pandas as pd

def how_many_medals(data: pd.DataFrame, name: str):
    participation = [x for x in range(len(data)) if data["Name"][x] == name]
    medals = {data["Year"][x]: {"G":0,"S":0,"B":0} for x in participation}
    for i in participation:
        if data["Medal"][i] == "Gold":
            medals[data["Year"][i]]["G"] += 1
        elif data["Medal"][i] == "Silver":
            medals[data["Year"][i]]["S"] += 1
        elif data["Medal"][i] == "Bronze":
            medals[data["Year"][i]]["B"] += 1
    return medals