stats = {'facebook': 55, 'yandex': 120, 'vk': 115,
    'google': 99, 'email': 42, 'ok': 98}

max_channel = max(stats, key=stats.get)

print(f"{max_channel}: {stats[max_channel]}")