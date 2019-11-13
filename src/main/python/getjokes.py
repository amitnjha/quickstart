import requests
import json

#json = requests.get("http://localhost:8080/joke")

for i in range(50):
    resp = requests.get("http://localhost:8080/joke")
    print(json.loads(resp.content.decode("utf-8")).get('joke'))
    print("\n")
