import urllib.request
import json

BASE_URL = "https://swapi.info/api"
HEADERS = {"User-Agent": "Mozilla/5.0"}


def _fetch(endpoint: str):
    url = f"{BASE_URL}/{endpoint}"
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode("utf-8"))


def get_films():
    try:
        for film in _fetch("films"):
            print(f"Title: {film['title']}")
            print(f"Episode: {film['episode_id']}")
            print(f"Director: {film['director']}")
            print(f"Producer: {film['producer']}")
            print(f"Release date: {film['release_date']}")
            print("-" * 40)
    except Exception as e:
        print(f"Error: {e}")


def get_people():
    try:
        for person in _fetch("people"):
            print(f"Name: {person['name']}")
            print(f"Height: {person['height']}")
            print(f"Mass: {person['mass']}")
            print(f"Gender: {person['gender']}")
            print("-" * 40)
    except Exception as e:
        print(f"Error: {e}")


def get_planets():
    try:
        for planet in _fetch("planets"):
            print(f"Name: {planet['name']}")
            print(f"Climate: {planet['climate']}")
            print(f"Population: {planet['population']}")
            print(f"Terrain: {planet['terrain']}")
            print("-" * 40)
    except Exception as e:
        print(f"Error: {e}")


def get_species():
    try:
        for s in _fetch("species"):
            print(f"Name: {s['name']}")
            print(f"Classification: {s['classification']}")
            print(f"Designation: {s['designation']}")
            print(f"Language: {s['language']}")
            print("-" * 40)
    except Exception as e:
        print(f"Error: {e}")


def get_vehicles():
    try:
        for v in _fetch("vehicles"):
            print(f"Name: {v['name']}")
            print(f"Model: {v['model']}")
            print(f"Manufacturer: {v['manufacturer']}")
            print(f"Vehicle class: {v['vehicle_class']}")
            print("-" * 40)
    except Exception as e:
        print(f"Error: {e}")


def get_starships():
    try:
        for s in _fetch("starships"):
            print(f"Name: {s['name']}")
            print(f"Model: {s['model']}")
            print(f"Manufacturer: {s['manufacturer']}")
            print(f"Starship class: {s['starship_class']}")
            print("-" * 40)
    except Exception as e:
        print(f"Error: {e}")
