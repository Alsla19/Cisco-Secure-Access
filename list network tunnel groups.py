import requests
import pprint
import json
url = "https://api.sse.cisco.com/deployments/v2/networktunnelgroups"

#Make sure to use the correct Bearer Token
BT = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

headers = { 'Authorization':f"Bearer {BT}"
,"Accept": "application/json" }

response = requests.request('GET', url, headers=headers)

json_object = json.loads(response.content)
pprint.pprint(json_object)