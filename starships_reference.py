import requests
from pprint import pprint
from pymongo import MongoClient


API_URL = "https://swapi.info/api/starships"
MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "starwars"

def get_starships():
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    return response.json()


def get_pilot_object_ids(db, pilot_urls):
    pilot_ids = []

    for pilot_url in pilot_urls:
        pilot = requests.get(pilot_url, timeout=10)
        pilot.raise_for_status()
        pilot_name = pilot.json()["name"]

        character = db.characters.find_one(
            {"name": pilot_name},
            {"_id": 1, "name": 1}
        )

        if character:
            pilot_ids.append(character["_id"])

    return pilot_ids

def transform_starships(db, starships):
    transformed_starships = []

    for starship in starships:
        starship["pilots"] = get_pilot_object_ids(
            db,
            starship.get("pilots", [])
        )
        transformed_starships.append(starship)

    return transformed_starships

def main():
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]

    starships = get_starships()
    transformed_starships = transform_starships(db, starships)

    db.starships.delete_many({})
    db.starships.insert_many(transformed_starships)

    print("Starships inserted:", db.starships.count_documents({}))
    pprint(
        list(
            db.starships.find(
                {"pilots": {"$ne": []}},
                {"_id": 0, "name": 1, "pilots": 1}
            ).limit(5)
        )
    )
    pprint(db.starships.find_one({}, {"name": 1, "pilots": 1}))

if __name__ == "__main__":
    main()

