import requests
import pokebase as pb
import json

name = 35
url = f'https://pokeapi.co/api/v2/pokemon/{name}/'

response = requests.get(url)
if response.status_code == 200:
    pokemon_data = response.json()
    print(f"Name: {pokemon_data['name']}")
    print(f"Height: {pokemon_data['height']}")
    print(f"Weight: {pokemon_data['weight']}")
    print("Abilities:")
    for ability in pokemon_data['abilities']:
        print(f"- {ability['ability']['name']}")
else:
    print(f"Error: {response.status_code}")
