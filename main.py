from pip._vendor import requests
import json
from pprint import pprint
def get_the_smartest_superhero() -> str:
    hero_int = {'Hulk' : 0, 'Captain America' : 0, 'Thanos' : 0}
    heroes_list = ['Hulk', 'Captain america', 'Thanos']
    intelligence_hero = ()
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    response = requests.get(url)
    bod = json.loads(response.content)
    for s in heroes_list:
        for i in s:
            if i in bod:
                intelligence_hero = bod[i]['powerstats']['intelligence']
                hero_int[i] = intelligence_hero        
    
    
    return print(hero_int)

get_the_smartest_superhero()