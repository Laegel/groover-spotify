import base64
import os
import requests

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

def fetch_token():
    encoded_credentials = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    response = requests.post("https://accounts.spotify.com/api/token", headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic " + encoded_credentials
    }, data={
        "grant_type": "client_credentials"
    })
    return response.json()["access_token"]


def fetch_latest_releases():
    token = fetch_token()
    response = requests.get("https://api.spotify.com/v1/browse/new-releases", headers={
        "Authorization": "Bearer " + token
    })
    # Could also loop until response["next"] is null to make sure to fetch all artists
    return response.json()