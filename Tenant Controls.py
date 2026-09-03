import requests
import json
import pprint

url = "https://api.sse.cisco.com/policies/v2/tenantControls/profiles"

#Make sure to use the correct Bearer Token
BT = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
payload = None

headers = { "Authorization":f"Bearer {BT}",
			"Accept": "application/json" }

response = requests.request('GET', url, headers=headers, data = payload)
output_json = json.loads(response.content)

pprint.pprint(output_json)


