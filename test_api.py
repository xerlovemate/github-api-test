import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение данных из переменных окружения
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
REPO_NAME = os.getenv('REPO_NAME')

# Базовый URL для работы с GitHub API
BASE_URL = 'https://api.github.com'

# Заголовки с токеном авторизации
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}


def create_repo():
    """Создание нового репозитория"""
    url = f'{BASE_URL}/user/repos'
    data = {
        'name': REPO_NAME,
        'private': False,  # Создание публичного репозитория
    }
    response = requests.post(url, json=data, headers=HEADERS)

    if response.status_code == 201:
        print(f'Repository {REPO_NAME} created successfully.')
    else:
        print(f'Error creating repository: {response.status_code}, {response.text}')


def check_repo_exists():
    """Проверка наличия репозитория"""
    url = f'{BASE_URL}/users/{GITHUB_USERNAME}/repos'
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        repos = response.json()
        repo_names = [repo['name'] for repo in repos]
        if REPO_NAME in repo_names:
            print(f'Repository {REPO_NAME} exists.')
        else:
            print(f'Repository {REPO_NAME} not found.')
    else:
        print(f'Error fetching repositories: {response.status_code}, {response.text}')


def delete_repo():
    """Удаление репозитория"""
    url = f'{BASE_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}'
    response = requests.delete(url, headers=HEADERS)

    if response.status_code == 204:
        print(f'Repository {REPO_NAME} deleted successfully.')
    else:
        print(f'Error deleting repository: {response.status_code}, {response.text}')


if __name__ == '__main__':
    # Шаги теста
    create_repo()  # 1. Создаем репозиторий
    check_repo_exists()  # 2. Проверяем, что он создан
    delete_repo()  # 3. Удаляем репозиторий
