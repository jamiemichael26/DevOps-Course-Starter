import requests
from flask import session

def get_apikeys():
    with open('todo_app\\data\\key.gitignore') as f:
            data = f.read().split("\n")
    return {'key': data[0], 'token': data[1]}

def get_items():
    apikey = get_apikeys()
    url = "https://api.trello.com/1/boards/c7trSbnB/cards"

    response = requests.request("GET",url,params=apikey)

    return response.json()

def complete_item(id):
    apikey = get_apikeys()

    url = "https://api.trello.com/1/cards/" + id

    headers = {
    "Accept": "application/json"
    }

    apikey.update({'idList': '5f5be2d2c3c4723ac911bbcb'})
    query = apikey

    requests.request(
    "PUT",
    url,
    headers=headers,
    params=query
    )

def add_item(title):
    apikey = get_apikeys()
    url = "https://api.trello.com/1/cards"

    apikey.update({'idList': '5f5be2d2c3c4723ac911bbc9','name': title})
    query = apikey

    requests.request(
    "POST",
    url,
    params=query
    )

def doing_item(id):
    apikey = get_apikeys()

    url = "https://api.trello.com/1/cards/" + id

    headers = {
    "Accept": "application/json"
    }

    apikey.update({'idList': '5f5be2d2c3c4723ac911bbca'})
    query = apikey

    requests.request(
    "PUT",
    url,
    headers=headers,
    params=query
    )

