# A list of dictionaries
people = [
    {"name":"noori","age":29,"city":"sirsa","role":"frontend dev"},
    {"name":"nitish","age":30,"city":"chandigarh","role":"research analyst"},
    {"name":"ekta","age":29,"city":"sirsa","role":"digital marketing expert"},
    {"name":"radhika","age":28,"city":"toronto","role":"beauty advisor"}
]

#print everyone
print("all", people)
# Total count
print("total",len(people))
# Access specific items
print("role of first person is", f"{people[0]["role"]}")
print("name of third person is", f"{people[2]["name"]}")
# Add a new person
people.append({"name":"niki","age":28,"city":"sydney","role":"pega developer"})
print("newly added person",f"{people[-1]}")
# Update a person's age
people[0]["age"] = 30
print("updated people",people)
# Print just the names (very common pattern)
for person in people:
    print(f"{person["name"]}")


#print everyone from sirsa
sirsa_names = []
for person in people:
    if person["city"] == "sirsa":
        sirsa_names.append(person["name"])
print(f"People from sirsa: {sirsa_names}")
print(f"People from sirsa: {', '.join(sirsa_names)}")

#Update radhika's role to skincare speciallist
found = False
for person in people:
    if person["name"] =="radhika":
        person["role"] = "skin specialist"
        print(f"updated person: {person}")
        found=True
        break
if found:
    print("updated list",people)
else :
    print("name doesnot exist")


# calculate avg age
total = 0
for person in people:
    total = total + person["age"]

avg= total/len(people)
print("avg age",avg)