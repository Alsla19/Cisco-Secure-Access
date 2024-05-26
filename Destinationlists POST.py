import requests
import json
import pprint

url = "https://api.sse.cisco.com/policies/v2/destinationlists"
BT = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjcyNmI5MGUzLWQ1MjYtNGMzZS1iN2QzLTllYjA5NWU2ZWRlOSIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1bWJyZWxsYS1hdXRoei9hdXRoc3ZjIiwic3ViIjoib3JnLzgyMTgwODQvY2xpZW50LzJlMDBjMzQ3ZTA5NjQzMWI4MWFiN2JlNjNjMTYxZDk2IiwiZXhwIjoxNzA4NDM0MDg3LCJuYmYiOjE3MDg0MzA0ODcsImlhdCI6MTcwODQzMDQ4Nywic2NvcGUiOiJkZXBsb3ltZW50cy5uZXR3b3Jrczp3cml0ZSBkZXBsb3ltZW50cy5uZXR3b3JrczpyZWFkIGRlcGxveW1lbnRzLnJvYW1pbmdjb21wdXRlcnM6d3JpdGUgZGVwbG95bWVudHMucm9hbWluZ2NvbXB1dGVyczpyZWFkIGRlcGxveW1lbnRzLmludGVybmFsbmV0d29ya3M6d3JpdGUgZGVwbG95bWVudHMuaW50ZXJuYWxuZXR3b3JrczpyZWFkIGRlcGxveW1lbnRzLmludGVybmFsZG9tYWluczp3cml0ZSBkZXBsb3ltZW50cy5pbnRlcm5hbGRvbWFpbnM6cmVhZCBkZXBsb3ltZW50cy52aXJ0dWFsYXBwbGlhbmNlczp3cml0ZSBkZXBsb3ltZW50cy52aXJ0dWFsYXBwbGlhbmNlczpyZWFkIGRlcGxveW1lbnRzLnNpdGVzOndyaXRlIGRlcGxveW1lbnRzLnNpdGVzOnJlYWQgZGVwbG95bWVudHMuZGF0YWNlbnRlcnM6cmVhZCBkZXBsb3ltZW50cy50dW5uZWxzOndyaXRlIGRlcGxveW1lbnRzLnR1bm5lbHM6cmVhZCBkZXBsb3ltZW50cy5uZXR3b3JrZGV2aWNlczp3cml0ZSBkZXBsb3ltZW50cy5uZXR3b3JrZGV2aWNlczpyZWFkIGRlcGxveW1lbnRzLnBvbGljaWVzOndyaXRlIGRlcGxveW1lbnRzLnBvbGljaWVzOnJlYWQgZGVwbG95bWVudHMucmVnaXN0ZXJlZGFwcGxpYW5jZXM6d3JpdGUgZGVwbG95bWVudHMucmVnaXN0ZXJlZGFwcGxpYW5jZXM6cmVhZCBkZXBsb3ltZW50cy5uZXR3b3JrdHVubmVsZ3JvdXBzOndyaXRlIGRlcGxveW1lbnRzLm5ldHdvcmt0dW5uZWxncm91cHM6cmVhZCBkZXBsb3ltZW50cy5yZWdpb25zOnJlYWQgZGVwbG95bWVudHMuY29ubmVjdG9yYWdlbnQ6d3JpdGUgZGVwbG95bWVudHMudGFnZGV2aWNlczp3cml0ZSBkZXBsb3ltZW50cy50YWdkZXZpY2VzOnJlYWQgZGVwbG95bWVudHMudGFnczp3cml0ZSBkZXBsb3ltZW50cy50YWdzOnJlYWQgcG9saWNpZXMuZGVzdGluYXRpb25saXN0czp3cml0ZSBwb2xpY2llcy5kZXN0aW5hdGlvbmxpc3RzOnJlYWQgcG9saWNpZXMuZGVzdGluYXRpb25zOndyaXRlIHBvbGljaWVzLmRlc3RpbmF0aW9uczpyZWFkIHBvbGljaWVzLmRscGluZGV4ZXI6d3JpdGUgcG9saWNpZXMuZGxwaW5kZXhlcjpyZWFkIHBvbGljaWVzLnJ1bGVzOndyaXRlIHBvbGljaWVzLnJ1bGVzOnJlYWQgcmVwb3J0cy5ncmFudWxhcmV2ZW50czpyZWFkIHJlcG9ydHMudXRpbGl0aWVzOnJlYWQgcmVwb3J0cy5hZ2dyZWdhdGlvbnM6d3JpdGUgcmVwb3J0cy5hZ2dyZWdhdGlvbnM6cmVhZCByZXBvcnRzLmN1c3RvbWVyczp3cml0ZSByZXBvcnRzLmN1c3RvbWVyczpyZWFkIHJlcG9ydHMuYXBwZGlzY292ZXJ5OndyaXRlIHJlcG9ydHMuYXBwZGlzY292ZXJ5OnJlYWQgcmVwb3J0cy5hcGl1c2FnZTpyZWFkIHJlcG9ydHMudXNhZ2UuaW5nZXN0OndyaXRlIHJlcG9ydHMudXNhZ2UubWV0cmljczpyZWFkIHJlcG9ydHMudXNhZ2Uuc3RhdHVzOnJlYWQgcmVwb3J0cy5wcml2YXRlcmVzb3VyY2VzOnJlYWQgcmVwb3J0cy5zdW1tYXJpZXNieXJ1bGU6cmVhZCIsImF1dGh6X2RvbmUiOmZhbHNlfQ.TjcdiodjuR_os88XKQ5AL9vf6u17ZmbhtNT0Ltjk63Avp5BrkHRvK4T7bhuF8YzuxwKPkslYfuI6GAALNVjC1aOBl3gZsPLMeJ46HZ1yQ18mI6MmboRvgQge5VP7Y88jzPQ2OotFBWHuQJVPXsWDiruUiwutbNk9v5cufV0O26-ew-ONUp5uDZaLgWUeIVofjnDKlrdQpYjCJrPgf2XkZ6rZXU1ZIsILjtGE-bYDnz9htX36qQIpCMlEYEn1j1CghRw8nLXb6ZzNOttx2uWCUfBuj51bOKA9O_CU8czFPseLD6sO8f9WGkn73OUEeVr2-qLyu1wIhndpg3BOOHtk3Q"

payload = '''{
    "access": "none",
    "isGlobal": false,
    "name": "The Network Viking"
}'''

headers = {
    "Authorization":f"Bearer {BT}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.request('POST', url, headers=headers, data = payload)

json_object = json.loads(response.content)
pprint.pprint(json_object)