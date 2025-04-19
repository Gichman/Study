queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]

word_count_stats = {}

for query in queries:
    word_count = len(query.split())
    word_count_stats[word_count] = word_count_stats.get(word_count, 0) + 1

total_queries = len(queries)

for word_count, count in sorted(word_count_stats.items()):
    percent = round((count / total_queries) * 100, 2)
    print(f"Запросов из {word_count} слов: {percent}%")