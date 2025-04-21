import requests


class VKUser:
    API_BASE_URL = 'https://api.vk.com/method/'

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id
        self.first_name = ""
        self.last_name = ""

    def get_friends(self):
        """Получает список друзей пользователя."""
        params = {
            'access_token': self.token,
            'user_id': self.user_id,
            'v': '5.131',
            'fields': 'first_name,last_name',
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

        my_friends_ids = {friend['id'] for friend in my_friends}
        other_friends_ids = {friend['id'] for friend in other_friends}

        common_ids = my_friends_ids & other_friends_ids

        common_friends_users = []
        for friend in my_friends:
            if friend['id'] in common_ids:
                common_friend = VKUser(self.token, friend['id'])
                common_friend.first_name = friend.get('first_name', '')
                common_friend.last_name = friend.get('last_name', '')
                common_friends_users.append(common_friend)

        return common_friends_users

    def __str__(self):
        """Возвращает ссылку на профиль пользователя VK."""
        return f"https://vk.com/id{self.user_id}"


# Пример использования
if __name__ == "__main__":
    TOKEN = "вставить_токен"  # Замените на актуальный токен!
    USER1_ID = 2004812878  # ID первого пользователя
    USER2_ID = 7324631124  # ID второго пользователя

    user1 = VKUser(TOKEN, USER1_ID)
    user2 = VKUser(TOKEN, USER2_ID)

    user1.first_name = "Иван"  #
    user1.last_name = "Иванов"
    user2.first_name = "Петр"
    user2.last_name = "Петров"

    # Используем оператор & для поиска общих друзей
    common_friends = user1 & user2

    print(f"Ссылка на профиль user1: {user1}")
    print(f"Ссылка на профиль user2: {user2}")

    if not common_friends:
        print("Нет общих друзей или возникла ошибка.")
    else:
        print(f"\nОбщие друзья между {user1.first_name} и {user2.first_name}:")
        for i, friend in enumerate(common_friends, 1):
            print(f"{i}. {friend}")