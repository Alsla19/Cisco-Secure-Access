import requests
import pprint
import json

url = "https://api.sse.cisco.com/policies/v2/destinationlists"

#Make sure to use the Bearer Token that you have generated:
BT = "Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

headers = { 'Authorization':BT
,"Accept": "application/json" }

response = requests.request('GET', url, headers=headers)

json_object = json.loads(response.content)

x=1
for item in json_object["data"]:
	print(f"Destination List -- {x}")
	pprint.pprint(f"Name: {item['name']}")
	pprint.pprint(f"ID: {item["id"]}")
	pprint.pprint(f"Destinations: {item["meta"]["destinationCount"]}")
	print("\n")
	x+=1

	