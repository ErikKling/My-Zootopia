import os
from dotenv import load_dotenv
import requests


load_dotenv()
base_url = "https://api.api-ninjas.com/v1/animals"
api_key = os.getenv("API_KEY")


def load_data_from_api(animal):
    '''Loads data from animals api and returns its contents.'''
    params = {
    "name": animal,
    "X-Api-Key": api_key
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    return data