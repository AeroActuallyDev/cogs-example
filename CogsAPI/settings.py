from . import request

def fetch_settings(client):
    settings = request.get(client, f"/{client.selfbot_name}/account/settings/").json()
    return settings

def fetch_account(client):
    return request.get(client, f"/{client.selfbot_name}/account/").json()

def push(client, settings):
    """
    Overwrite all settings
    """
    return request.post(client, f"/{client.selfbot_name}/account/settings/", json={"settings": settings}).json()