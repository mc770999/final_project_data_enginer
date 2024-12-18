from dataclasses import asdict

from mongo_db.database import db
from mongo_db.models.date_model import Date
from mongo_db.models.event_model import Event
from mongo_db.models.location_model import Location
from mongo_db.models.target_type_model import TargetType

event_collection = db["events"]

def create_event(event: Event):
    event_dict = asdict(event)
    event_dict["location"] = asdict(event.location)
    event_dict["date"] = asdict(event.date)
    event_dict["target_types"] = [asdict(t) for t in event.target_types]
    event_collection.insert_one(event_dict)


def read_event(event_id: str) -> Event:
    result = event_collection.find_one({"event_id": event_id})
    if result:
        location = Location(**result["location"])
        target_types = [TargetType(**t) for t in result["target_types"]]
        return Event(
            event_id=result["event_id"],
            num_kill=result["num_kill"],
            num_wound=result["num_wound"],
            number_of_casualties_calc=result["number_of_casualties_calc"],
            date=Date(**result["date"]),
            summary= result["summary"],
            num_preps=result["num_preps"],
            location=location,
            attack_type=result["attack_type"],
            target_types=target_types,
            group_name=result["group_name"]
        )
    return None


def update_event(event_id: str, updated_data: dict):
    event_collection.update_one({"event_id": event_id}, {"$set": updated_data})


def delete_event(event_id: str):
    event_collection.delete_one({"event_id": event_id})