import pytest
import yaml
import requests


with open('config.yaml') as file:
    my_dict=yaml.safe_load(file)

url = my_dict['url']
url1 = my_dict['url1']


@pytest.fixture()
def login():
    obj_data = requests.post(url=url, data={'username':'AlexeyZ2', 'password': 'd885569a6b'})
    token = obj_data.json()['token']
    return token

@pytest.fixture()
def postP():
    obj_data = requests.post(url=url1, headers={"X-Auth-Token": my_dict['token']},data={
        'username':'AlexeyZ2',
        'password': 'd885569a6b',
        'title': 'newTitle',
        'description': 'Anything',
        'content':'oh my Gosh'})
    return obj_data.json()['description']
