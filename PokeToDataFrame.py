import requests
import pandas as pd
import sqlalchemy as db

url = 'https://pokeapi.co/api/v2/pokemon'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
else:
    print(f"Error: {response.status_code}")

pokemon_list = []
for pokemon in data['results']:
    pokemon_list.append(pokemon['name'])

df = pd.DataFrame(pokemon_list, columns=['Pokemon'])

engine = db.create_engine('sqlite:///PokemonDB.db')

df.to_sql('pokemon_table', con=engine, if_exists='replace', index=False)
with engine.connect() as connection:
    query_result = connection.execute(db.text("SELECT * FROM pokemon_table;")).fetchall()
    print(pd.DataFrame(query_result))
