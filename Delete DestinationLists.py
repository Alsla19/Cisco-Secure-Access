import requests
import json
import pprint

url = "https://api.sse.cisco.com/policies/v2/destinationlists/17657001"
#Add your token as a string to the variable BT
BT = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

payload = '''{
    "access": "none",
    "isGlobal": false,
    "name": "The Network Viking3"
}'''

headers = {
    "Authorization":f"Bearer {BT}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.request('DELETE', url, headers=headers, data = payload)

json_object = json.loads(response.content)
pprint.pprint(json_object)