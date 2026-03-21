import requests

session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0"
}

def get(url):
    return session.get(url, headers=headers, timeout=5)

def post(url, data):
    return session.post(url, data=data, headers=headers, timeout=5)
