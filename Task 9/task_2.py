import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.base_url = 'https://cloud-api.yandex.net/v1/disk/resources'

    def get_headers(self):
        return {
            'Authorization': f'OAuth {self.token}'
        }

    def upload(self, file_path: str):
        """Метод загружает файл file_path на яндекс диск"""
        file_name = os.path.basename(file_path)  
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

        params = {
            'path': file_name,
            'overwrite': 'true'
        }

        response = requests.get(upload_url, headers=self.get_headers(), params=params)
        if response.status_code != 200:
            return f'Ошибка получения ссылки: {response.status_code}, {response.text}'

        href = response.json().get('href')

        with open(file_path, 'rb') as f:
            upload_response = requests.put(href, files={'file': f})

        if upload_response.status_code == 201:
            return '✅ Файл успешно загружен на Яндекс.Диск!'
        else:
            return f'❌ Ошибка загрузки: {upload_response.status_code}, {upload_response.text}'


if __name__ == '__main__':
    # Вставить путь к файлу ниже
    file_path = r'C:\Users\Ghost\Downloads\recipes.txt'
    # Вставить токен
    uploader = YaUploader('put_here_your_token')
    result = uploader.upload(file_path)
    print(result)