from pip._vendor import requests
import json
def get_the_smartest_superhero() -> str:
    hero_int = {}
    heroes_list = ['Thanos', 'Hulk', 'Captain America',]
    intelligence_hero = ()
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    all_heroes = requests.get(url).json()
    for hero in all_heroes:
        if hero['name'] in heroes_list:
            intelligence_hero = int(hero['powerstats']['intelligence'])
            hero_int[hero['name']] = intelligence_hero
    the_smartest_superhero = list(hero_int.keys())
    return print(the_smartest_superhero[-1])
    

get_the_smartest_superhero()