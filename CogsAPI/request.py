import requests
from os import getenv, path

def base():
    """
    Get base address of CogsAPI server.
    """
    return f"{getenv('HTTP_SCHEME')}://{getenv('MASTER_SERVER')}"

def post(client, url, json={}, headers=None):
    """
    Post to the the CogsAPI server.
    """
    headers = {"authorization": client.whitelist} if headers is None else headers
    return requests.post(f"{getenv('HTTP_SCHEME')}://{getenv('MASTER_SERVER')}{url}", json=json, headers=headers)

def get(client, url, json={}, headers=None):
    """
    Fetch from the CogsAPI server.
    """
    headers = {"authorization": client.whitelist} if headers is None else headers
    return requests.get(f"{getenv('HTTP_SCHEME')}://{getenv('MASTER_SERVER')}{url}", json=json, headers=headers)

    