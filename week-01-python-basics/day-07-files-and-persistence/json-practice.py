import json

# ---- Saving a list of dictionaries to JSON ----
contacts = [
    {"name":"noori","phone":"8684999666","city":"sirsa"},
    {"name":"nitish","phone":"999999999","city":"chd"},
    {"name":"noori","phone":"8888888888","city":"sirsa"}
]

# write a list to a json file
with open("contacts.json","w") as file:
    json.dump(contacts,file, indent=2)

# indent 2 is for pretty print json

print("Saved contacts.json")

# --- Reading it back ---
with open("contacts.json","r") as file:
    loaded_contacts = json.load(file)

print("Loaded:")
print(loaded_contacts)
print(f"number of contacts:{len(loaded_contacts)}")

# --- Verify its a real Python list ---
print(f"\nType: {type(loaded_contacts)}")
print(f"\nFirst contact's name: {loaded_contacts[0]['name']}")




me = {
    "name":"Noori",
    "age": 29,
    "city":"sirsa",
    "skills":["React","JavaScript","Python"],
    "currently_learning":"AI Engineering"
}

with open("about_me.json","w") as file:
    json.dump(me,file, indent=2)

print("Saved about me details")
    
with open("about_me.json","r") as file:
    detail = json.load(file)

print("Loaded")
print(detail)
print("name: ",detail["name"])
print("No. of skills: ", len(detail["skills"]))