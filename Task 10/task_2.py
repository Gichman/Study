import requests


class VKUser:
    API_BASE_URL = 'https://api.vk.com/method/'

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def get_friends(self):
        """Получает список друзей пользователя."""
        params = {
            'access_token': self.token,
            'user_id': self.user_id,
            'v': '5.131',
            'fields': 'first_name,last_name',  # Добавляем имена и фамилии
        }
        try:
            response = requests.get(f"{self.API_BASE_URL}friends.get", params=params)
            data = response.json()

            if 'error' in data:
                error_msg = data['error']['error_msg']
                if "access denied" in error_msg.lower():
                    return []  # Профиль закрыт
                raise Exception(f"VK API Error: {error_msg}")

            return data['response']['items']
        except Exception as e:
            print(f"Ошибка при запросе друзей: {e}")
            return []

    def __and__(self, other_user):
        """Перегрузка оператора & для поиска общих друзей."""
        my_friends = self.get_friends()
        other_friends = other_user.get_friends()

        if not my_friends or not other_friends:
            print("Не удалось получить списки друзей (возможно, профили закрыты).")
            return []

        # Получаем множества ID друзей
        my_friends_ids = {friend['id'] for friend in my_friends}
        other_friends_ids = {friend['id'] for friend in other_friends}

        # Находим пересечение
        common_ids = my_friends_ids & other_friends_ids

        # Создаем список экземпляров VKUser для общих друзей
        common_friends_users = []
        for friend in my_friends:
            if friend['id'] in common_ids:
                # Создаем новый экземпляр VKUser для каждого общего друга
                common_friend = VKUser(self.token, friend['id'])
                # Добавляем имя и фамилию (если нужно)
                common_friend.first_name = friend.get('first_name', '')
                common_friend.last_name = friend.get('last_name', '')
                common_friends_users.append(common_friend)

        return common_friends_users

    def __str__(self):
        """Для красивого вывода информации о пользователе."""
        return f"{getattr(self, 'first_name', '?')} {getattr(self, 'last_name', '?')} (id{self.user_id})"


# Пример использования
if __name__ == "__main__":
    TOKEN = "вставить_токен"  # Замените на актуальный токен!
    USER1_ID = 2002481878  # ID первого пользователя
    USER2_ID = 7324633124  # ID второго пользователя

    user1 = VKUser(TOKEN, USER1_ID)
    user2 = VKUser(TOKEN, USER2_ID)

    # Используем оператор & для поиска общих друзей
    common_friends = user1 & user2

    if not common_friends:
        print("Нет общих друзей или возникла ошибка.")
    else:
        print(f"Общие друзья между {user1} и {user2}:")
        for i, friend in enumerate(common_friends, 1):
            print(f"{i}. {friend}")