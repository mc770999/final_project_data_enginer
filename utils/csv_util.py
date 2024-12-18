from itertools import count

import pandas as pd
import toolz as t
from mongo_db.models.event_model import Event
from mongo_db.models.location_model import Location
from mongo_db.models.target_type_model import TargetType
from typing import List



def split_into_chunks(lst, chunk_size):
    return list(t.partition_all(chunk_size, lst))


def convert_to_target_types(row):
    target_types = []
    count = 1
    for targtype in ["targtype1", "targtype2", "targtype3"]:
        if not pd.isna(row[targtype]):
            target_types.append(TargetType(target_type=targtype, target=row[f"target{count}"]))
        count += 1

    return target_types

def convert_to_group_names(row):
    group_names = []
    for group_name in ["gname", "gname2", "gname3"]:
        if not pd.isna(row[group_name]) and row[group_name].lower() != "unknown":
            group_names.append(group_name)
    return group_names

def convert_to_attack_type(row):
    attack_types_txt = []
    for attack_type_txt in ["attacktype1_txt", "attacktype2_txt", "attacktype3_txt"]:
        if not pd.isna(row[attack_type_txt]):
            attack_types_txt.append(attack_type_txt)
    return attack_types_txt






def process_csv(file_path: str) -> List[Event]:
    # Load CSV file
    df = pd.read_csv(file_path, encoding="iso-8859-1")


    df[["nperps", "nkill", "nwound"]] = (
        df[["nperps", "nkill", "nwound"]]
        .fillna(0)
        .where(df[["nperps", "nkill", "nwound"]] > 0, 0)
    )

    print(5)
    print(df[["iyear", "imonth", 'iday']])

    df.rename(columns={
        'eventid': 'event_id',
        'iyear': 'year',
        'imonth': 'month',
        'iday': 'day',
        'country_txt': 'country_name',
        'region_txt': 'region_txt',
        'city': 'city',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'nkill': 'num_kill',
        'nwound': 'num_wound',
        "npreps" : "num_preps"
    }, inplace=True)

    # Filter necessary columns


    events = []
    for _, row in df.iterrows():
        location = Location(
            country_name=row['country_name'],
            region_txt=row['region_txt'],
            city=row['city'],
            latitude=row['latitude'],
            longitude=row['longitude']
        )

        event = Event(
            event_id=str(row['event_id']),
            num_kill=int(row['num_kill']) ,
            num_wound=int(row['num_wound']),
            number_of_casualties_calc=int(row['num_wound']) * 1 + int(row['num_kill']) * 2,
            date=f"{row['day']}/{row['month']}/{row['year']}",
            num_preps=row["num_preps"],
            location=location,
            attack_type=convert_to_attack_type(row),
            target_types=convert_to_target_types(row),
            group_name=convert_to_group_names(row)
        )
        events.append(event)


    return events

process_csv("../data/globalterrorismdb_0718dist-1000 rows.csv")