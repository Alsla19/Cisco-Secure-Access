import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth

token_url = 'https://api.sse.cisco.com/auth/v2/token'

client_id = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

def get_token(url, ident, secret):
    auth = HTTPBasicAuth(ident, secret)
    client = BackendApplicationClient(client_id=ident)
    oauth = OAuth2Session(client=client)
    return oauth.fetch_token(token_url=url, auth=auth)

token = get_token(token_url, client_id, client_secret)
print(f"Access Token = {token['access_token']}")