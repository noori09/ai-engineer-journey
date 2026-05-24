import requests
import json

url="https://icanhazdadjoke.com"
headers= {"Accept":"application/json"}

def fetch_jokes():
    response= requests.get(url,headers=headers)
    if response.status_code == 200:
            joke = response.json()["joke"]
            return joke
    else:
        return None
       
def load_jokes():
    try:
        with open("jokes.json","r") as file:
            return json.load(file)          
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: jokes.json is corrupted. Starting fresh.")
        return []

def save_jokes(jokes_list):
    with open("jokes.json","w") as file:
        json.dump(jokes_list,file ,indent=2)


# -------- main --------
existing_joke = load_jokes()
print("existing",existing_joke)
fetched_joke = fetch_jokes()
print("fetched",fetched_joke)
existing_joke.append(fetched_joke)
print("updated",existing_joke)
save_jokes(existing_joke)
print("New joke: ",fetched_joke)
print("Count: ", len(existing_joke))