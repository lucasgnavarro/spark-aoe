import requests

from app.settings import API_DOG_CEO_URL
from app.clients.exceptions import HttpServiceException

DOG_BREEDS_URL = f'{API_DOG_CEO_URL}/breeds/list/all'


def fetch_dog_breeds():

    response = requests.get(DOG_BREEDS_URL)
    if response.ok:
        json_response = response.json()
        return json_response.get('message') or {}
    else:
        raise HttpServiceException(f'Failed to get data from {DOG_BREEDS_URL}')
