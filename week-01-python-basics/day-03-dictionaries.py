# A dictionary about me

me={
"name": "Noori",
"age": 28,
"city":"Sirsa",
"profession": "Frontend Engineer",
"years of exp": 7,
}

#Access individual values
print("Name", me["name"])
print("city",me["city"])

#update a value
me["age"] = 29
print("updated age",me["age"])

#add a new key
me["learning"] = "GenAI Engineering"
print("after adding learning",me)

#safe access - trying a key that doesnot exists
print("email",me.get("email"))
print("email",me.get("email","not set yet"))


#check if a key exists
print("name","name" in me)
print("name",me.get("name"))
print("has salary","salary" in me)


#loop through everything
for key, value in me.items():
    print(f"{key} : {value}")


#delete a key
del me["years of exp"]
print("after del",me)