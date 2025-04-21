import json
from collections import Counter


def load_json_data(file_path):
    """Загружает данные из JSON-файла."""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def extract_texts_from_json(data):
    """Извлекает тексты новостей из JSON-структуры."""
    items = data['rss']['channel']['items']
    texts = [item['description'] for item in items]
    return texts


def process_texts(texts):
    """Обрабатывает тексты, выделяя слова длиннее 6 символов."""
    words = []
    for text in texts:
        words.extend(word.lower() for word in text.split() if len(word) > 6)
    return words


def get_top_words(words, top_size=10):
    """Возвращает топ самых часто встречающихся слов."""
    word_counts = Counter(words)
    return word_counts.most_common(top_size)


def main():
    file_path = 'newsafr.json'

    data = load_json_data(file_path)

    texts = extract_texts_from_json(data)

    words = process_texts(texts)

    top_words = get_top_words(words)

    print("Топ 10 слов длиннее 6 символов:")
    for i, (word, count) in enumerate(top_words, 1):
        print(f"{i}. {word}: {count} раз(а)")


if __name__ == "__main__":
    main()