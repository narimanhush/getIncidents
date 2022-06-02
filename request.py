import requests

B = "http://127.0.0.1:9000/"

response = requests.get(B + "incident" )

print(response.json())