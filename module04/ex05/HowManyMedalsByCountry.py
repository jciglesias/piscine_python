import pandas as pd
from copy import deepcopy

def how_many_medals_by_country(data: pd.DataFrame, country: str):
    team_sports = {'Basketball':[], 'Football':[],  'Tug-Of-War':[], 'Badminton':[], 'Sailing':[], 'Handball':[], 'Water Polo':[], 'Hockey':[], 'Rowing':[], 'Bobsleigh':[], 'Softball':[], 'Volleyball':[], 'Synchronized Swimming':[], 'Baseball':[], 'Rugby Sevens':[], 'Rugby':[], 'Lacrosse':[], 'Polo':[]}
    participants = [x for x in range(len(data)) if data["Team"][x] == country]
    medals = {data["Year"][x]: {"G":0,"S":0,"B":0} for x in participants}
    team = {data["Year"][x]: {"G":{"F":deepcopy(team_sports), "M":deepcopy(team_sports)},"S":{"F":deepcopy(team_sports), "M":deepcopy(team_sports)},"B":{"F":deepcopy(team_sports), "M":deepcopy(team_sports)}} for x in participants}
    for i in participants:
        if data["Medal"][i] == "Gold":
            if  data["Sport"][i] in team_sports:
                if  data["Event"][i] not in team[data["Year"][i]]["G"][data["Sex"][i]][data["Sport"][i]]:
                    medals[data["Year"][i]]["G"] += 1
                    team[data["Year"][i]]["G"][data["Sex"][i]][data["Sport"][i]].append(data["Event"][i])
            else:
                medals[data["Year"][i]]["G"] += 1
        elif data["Medal"][i] == "Silver":
            if  data["Sport"][i] in team_sports:
                if  data["Event"][i] not in team[data["Year"][i]]["S"][data["Sex"][i]][data["Sport"][i]]:
                    medals[data["Year"][i]]["S"] += 1
                    team[data["Year"][i]]["S"][data["Sex"][i]][data["Sport"][i]].append(data["Event"][i])
            else:
                medals[data["Year"][i]]["S"] += 1
        elif data["Medal"][i] == "Bronze":
            if  data["Sport"][i] in team_sports:
                if  data["Event"][i] not in team[data["Year"][i]]["B"][data["Sex"][i]][data["Sport"][i]]:
                    medals[data["Year"][i]]["B"] += 1
                    team[data["Year"][i]]["B"][data["Sex"][i]][data["Sport"][i]].append(data["Event"][i])
            else:
                medals[data["Year"][i]]["B"] += 1
    return dict(sorted(medals.items()))