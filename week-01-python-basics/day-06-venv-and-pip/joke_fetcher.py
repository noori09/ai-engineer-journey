import requests
url = "https://icanhazdadjoke.com"
headers = {"Accept": "application/json"}
for i in range(1,4):
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        joke = response.json()["joke"]
        print(f"Joke #{i}: {joke}")
        print()
    else:
       print(f"Request #{i} failed with status {response.status_code}")