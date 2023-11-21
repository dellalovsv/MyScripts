import requests


def get_page(url: str = None, data: dict = None, method: str = 'GET') -> requests.Response | None:
    global res
    if url is None:
        return None

    if data is not None:
        if method == 'GET':
            res = requests.get(url, data=data)
        if method == 'POST':
            res = requests.post(url, data=data)
    else:
        if method == 'GET':
            res = requests.get(url)
        if method == 'POST':
            res = requests.post(url)
    if res.status_code == 200:
        return res
    else:
        return None
