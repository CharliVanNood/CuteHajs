import requests

def request(url):
    response = requests.get(url)
    return response