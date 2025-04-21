import requests

TOKEN = '2619421814940190'
API_BASE = f'https://superheroapi.com/api/{TOKEN}'

heroes = ['Hulk', 'Captain America', 'Thanos']


def get_hero_id(name):
    url = f'{API_BASE}/search/{name}'
    response = requests.get(url)
    data = response.json()
    if response.ok and data['response'] == 'success':
        return data['results'][0]['id']
    else:
        raise ValueError(f'Не удалось найти ID для {name}')


def get_intelligence(hero_id):
    url = f'{API_BASE}/{hero_id}/powerstats'
    response = requests.get(url)
    data = response.json()
    if response.ok:
        return int(data['intelligence'])
    else:
        raise ValueError(f'Не удалось получить характеристики для ID {hero_id}')


def find_smartest_hero(hero_names):
    intelligence_scores = {}
    for name in hero_names:
        hero_id = get_hero_id(name)
        intelligence = get_intelligence(hero_id)
        intelligence_scores[name] = intelligence
        print(f'{name}: интеллект = {intelligence}')

    smartest = max(intelligence_scores, key=intelligence_scores.get)
    print(f'\nСамый умный супергерой: {smartest} 🧠')


if __name__ == '__main__':
    find_smartest_hero(heroes)