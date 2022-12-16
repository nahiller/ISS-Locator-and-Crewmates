import requests

def get_response():
    return requests.get("http://api.open-notify.org/astros.json").json()

def parse_response(json):
    return [person['name'] for person in json['people'] if person['craft'] == 'ISS']

def get_astronauts_names():
    return parse_response(get_response())
