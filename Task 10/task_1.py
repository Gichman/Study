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
            'v': '5.131',  # Актуальная версия API
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

    def get_common_friends(self, other_user):
        """Находит общих друзей."""
        my_friends = self.get_friends()
        other_friends = other_user.get_friends()

        if not my_friends or not other_friends:
            print("Не удалось получить списки друзей (возможно, профили закрыты).")
            return []

        my_friends_ids = {friend['id'] for friend in my_friends}
        other_friends_ids = {friend['id'] for friend in other_friends}

        common_ids = my_friends_ids & other_friends_ids

        common_friends = []
        for friend in my_friends:
            if friend['id'] in common_ids:
                common_friends.append(friend)

        return common_friends


# Пример использования
if __name__ == "__main__":
    TOKEN = "втавить_актуальный_токен"  # Замените на актуальный токен!
    USER1_ID = 159793860  # ID первого пользователя
    USER2_ID = 715253630  # ID второго пользователя

    user1 = VKUser(TOKEN, USER1_ID)
    user2 = VKUser(TOKEN, USER2_ID)

    common_friends = user1.get_common_friends(user2)

    if not common_friends:
        print("Нет общих друзей или возникла ошибка.")
    else:
        print(f"Общие друзья между пользователями {USER1_ID} и {USER2_ID}:")
        for i, friend in enumerate(common_friends, 1):
            name = f"{friend.get('first_name', '?')} {friend.get('last_name', '?')}"
            print(f"{i}. {name} (id{friend['id']})")