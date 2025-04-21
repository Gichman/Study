import requests
import time
from datetime import datetime, timedelta

def get_python_questions():
    to_date = int(time.time())
    from_date = int((datetime.now() - timedelta(days=2)).timestamp())

    url = 'https://api.stackexchange.com/2.3/questions'
    params = {
        'fromdate': from_date,
        'todate': to_date,
        'order': 'desc',
        'sort': 'creation',
        'tagged': 'python',
        'site': 'stackoverflow',
        'pagesize': 100
    }

    response = requests.get(url, params=params)
    data = response.json()

    if 'items' not in data:
        print("❌ Ошибка получения данных")
        return

    print("📌 Вопросы с тегом 'python' за последние 2 дня:\n")
    for item in data['items']:
        title = item['title']
        link = item['link']
        creation = datetime.fromtimestamp(item['creation_date']).strftime('%Y-%m-%d %H:%M')
        print(f"🟢 [{creation}] {title}\n➡️ {link}\n")

if __name__ == '__main__':
    get_python_questions()