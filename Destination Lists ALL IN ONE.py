from oauthlib.oauth2 import BackendApplicationClient
from oauthlib.oauth2 import TokenExpiredError
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
import time
import requests
import pprint
import json


def fetch_headers(BToken):
	BT = f"Bearer {BToken}"
	headers = { 'Authorization':BT,
			"Content-Type": "application/json",
			"Accept": "application/json" 
			}
	return headers

# GET OAUTH 2.0 TOKEN
def getToken():
	token_url = 'https://api.sse.cisco.com/auth/v2/token'
	try:
		#ASSIGN your client ID to the variable client_id and secret to the variable client_secret
		client_id = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
		client_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

		auth = HTTPBasicAuth(client_id, client_secret)
		client = BackendApplicationClient(client_id=client_id)
		oauth = OAuth2Session(client=client)
		token = oauth.fetch_token(token_url=token_url, auth=auth)
		print("######Token Generated Successfully######")
		return token
	except e as Exception:
		print(f"Encountered an error while Fetching the TOKEN :: {e}")


# 1 - GET DESTINATION LISTS
def fetch_destinationlists(h):
	url = "https://api.sse.cisco.com/policies/v2/destinationlists"
	try:
		response = requests.request('GET', url, headers=h)
		json_object = json.loads(response.content)

		#pprint.pprint(json_object)
		x=1
		for item in json_object["data"]:
			print(f"Destination List : {x}")
			pprint.pprint(f"Name : {item['name']}")
			pprint.pprint(f"ID : {item['id']}")
			#pprint.pprint(f"Destination Count : {item['meta']['destinationCount']}")
			print("\n")
			x+=1
	except e as Exception:
		print(f"Encountered an Error while Fetching the Destination Lists :: {e}")


# 2 - GET DESTINATION LIST
def get_destinationlist(h):
	try:
		choice = input("Enter the ID of the DestinationList:: ")
		url = "https://api.sse.cisco.com/policies/v2/destinationlists/" + choice
		response = requests.request('GET', url, headers=h)
		json_object = json.loads(response.content)
		print("\n\n")
		pprint.pprint(json_object)
		print("\n\n")
	except e as Exception:
		print(f"Encountered an Error while Fetching the Destination List Details :: {e}")


# 3 - CREATE DESTINATION LIST
def create_destinationlist(h):
	url = "https://api.sse.cisco.com/policies/v2/destinationlists"
	try:
		naav = input("Name of the DestinationList :: ")
		payload = {
		    "access": "none",
		    "isGlobal": False,
		    "name": naav,	
		    }
		response = requests.request('POST', url, headers=h, data = json.dumps(payload))
		json_object = json.loads(response.content)
		print("\n\n")
		pprint.pprint(json_object)
		print("\n\n")
	except e as Exception:
		print(f"Encountered an Error while Creating the Destination List :: {e}")


# 4 - UPDATE DESTINATION LIST NAME
def patch_destinationlist(h):
	try:
		choice = input("Enter the ID of the DestinationList for changing it's name :: ")
		url = "https://api.sse.cisco.com/policies/v2/destinationlists/" + choice
		naav = input("Enter New Name :: ")
		payload = {"name": naav}

		response = requests.request('PATCH', url, headers=h, data = json.dumps(payload))
		json_object = json.loads(response.content)
		print("\n\n")
		pprint.pprint(json_object)
		print("\n\n")
	except e as Exception:
		print(f"Encountered an Error while Updating the Destination List :: {e}")


# 5 - DELETE DESTINATION LIST
def delete_destinationlist(h):
	try:
		choice = input("Enter the ID of the DestinationList for DELETION :: ")
		url = "https://api.sse.cisco.com/policies/v2/destinationlists/" + choice

		response = requests.request('DELETE', url, headers=h)
		json_object = json.loads(response.content)
		print("\n\n")
		pprint.pprint(json_object)
		print("\n\n")
	except Exception as e:
		print(f"Encountered an Error while Deleting the Destination List :: {e}")


# 6 - GET DESTINATIONS FROM A DESTINATION LIST
def fetch_detail(h):
	try:
		choice = input("DestinationList ID: ")

		url2 = "https://api.sse.cisco.com/policies/v2/destinationlists/" + choice + "/destinations"

		response = requests.request('GET', url2, headers=h)
		print("\n")
		json_dest = json.loads(response.content)
		pprint.pprint(json_dest)
		print("\n\n")
	except e as Exception:
		print(f"Encountered an Error while Fetching the Destinations from the Destination List :: {e}")


# 7 - ADD DESTINATIONS TO A DESTINATION LIST
def add_destinations(h):
	try:
		choice = input("Enter the ID of the DestinationList :: ")
		url = "https://api.sse.cisco.com/policies/v2/destinationlists/" + choice + "/destinations"
		destination_to_add = input("\nEnter the destination that you want to add :: ")
		payload = [{"destination": destination_to_add}]
		
		response = requests.request('POST', url, headers=h, data = json.dumps(payload))
		print("\n")
		json_dest = json.loads(response.content)
		pprint.pprint(json_dest)
		print("\n\n")
	except e as Exception:
		print(f"Encountered an Error while Adding the Destination to the Destination List :: {e}")


# 8 - DELETE DESTINATIONS FROM DESTINATION LIST
def delete_entry(h):
	try:
		choice_del = input("\nCONFIRM DestinationList ID from which you want to delete the Destination :: ")
		url3 = "https://api.sse.cisco.com/policies/v2/destinationlists/" + choice_del + "/destinations/remove"
		dest = int(input("ID of the Destination that you want to remove: "))

		payload = f"[{dest}]"
		response = requests.request('DELETE', url3, headers=h, data=payload)
		json_del = json.loads(response.content)
		print("\n\n")
		pprint.pprint(json_del)
		print("\n\n")
	except e as Exception:
		print(f"Encountered an Error while Deleting a Destination from the Destination List :: {e}")



#FETCH COOKIE
possess_cookie = " "
while possess_cookie not in ["Y","y","N","n"]:
	possess_cookie = input("Token Already Generated? (Y/N) :: ")
	if possess_cookie.upper() =="N":
		cook = getToken()
		with open("cookie.txt","w") as wr:
			wr.writelines(cook["access_token"])
	#	print(f"Access Token = {cook["access_token"]}")


#FETCH HEADERS
with open("cookie.txt","r") as ree:
	h = fetch_headers(ree.readline())


print("\n")
while True:
	action = input("""Available operations:
1. Get Destination Lists
2. Get Destination List
3. Create Destination List
4. Update Destination List Name
5. Delete Destination List
6. Get Destinations from Destination List
7. Add Destinations to a Destination List
8. Delete Destinations from Destination List
9. Exit

Enter Your Choice :: """)

	print("\n")
	operation = action.replace(" ","")
	if operation == "1":
		fetch_destinationlists(h)

	elif operation == "2":
		fetch_destinationlists(h)
		get_destinationlist(h)

	elif operation == "3":
		create_destinationlist(h)

	elif operation == "4":
		fetch_destinationlists(h)
		patch_destinationlist(h)

	elif operation == "5":
		fetch_destinationlists(h)
		delete_destinationlist(h)

	elif operation == "6":
		fetch_destinationlists(h)
		fetch_detail(h)

	elif operation == "7":
		fetch_destinationlists(h)
		add_destinations(h)
	
	elif operation == "8":
		fetch_destinationlists(h)
		fetch_detail(h)
		delete_entry(h)

	elif operation == "9":
		break
	
	else:
		print("\n")
		print("==========INCORRECT INPUT==========")
		print("\n")

print("Thank You!!! Good Bye!!!")
time.sleep(5)
