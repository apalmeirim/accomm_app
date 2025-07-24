import json
from pathlib import Path
from app.database import SessionLocal
from app.models.city import City
from app.models.accommodation import Accommodation
from app.models.attraction import Attraction


db = SessionLocal()

def load_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def seed_data():
    # Load and insert cities
    cities_data = load_json("app/seed_test/cities.json")
    cities = []
    for city_info in cities_data:
        city = City(**city_info)
        db.add(city)
        cities.append(city)
    db.commit()
    for city in cities:
        db.refresh(city)

    # Map city names to IDs for foreign key assignment
    city_name_to_id = {city.name: city.id for city in cities}

    # Load and insert accommodations
    accommodations_data = load_json("app/seed_test/accommodations.json")
    for accom_info in accommodations_data:
        city_id = city_name_to_id.get(accom_info.pop("city_name"))
        accom = Accommodation(**accom_info, city_id=city_id)
        db.add(accom)
    db.commit()

    # Load and insert attractions
    attractions_data = load_json("app/seed_test/attractions.json")
    for attr_info in attractions_data:
        city_id = city_name_to_id.get(attr_info.pop("city_name"))
        attraction = Attraction(**attr_info, city_id=city_id)
        db.add(attraction)
    db.commit()
    db.close()

if __name__ == "__main__":
    seed_data()