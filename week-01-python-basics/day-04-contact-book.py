#A terminal program that lets the user manage contacts (name, phone, city). 
# It shows a menu, takes commands, and keeps running until the user quits.


# Requirements:

# Menu should show options 1-6:

# Add a contact
# List all contacts
# Search for a contact
# Update a contact's phone
# Delete a contact
# Quit


# After the user picks a number, print something like "You picked: Add" for now (no real functionality yet)
# If they pick 6, print goodbye and exit the loop
#If they enter something invalid (like "abc" or "99"), tell them and show the menu again

contact_menu = {
    "1": "Add a contact",
    "2": "List all contacts",
    "3": "Search for a contact",
    "4": "Update a contact's phone",
    "5": "Delete a contact",
    "6": "Quit"
}
contacts = []
while True:
    print("\n ======= Contact Menu ========")
    for key,value in contact_menu.items():
        print(f"\n {key}. {value}")
    option = input("Choose an option (1-6) : ").strip()
    if option == "1":
        name = input("Enter Contact's Name: ").strip()
        phone = input("Enter Contact's Mobile Number: ").strip()
        city = input("Enter Contact's City: ").strip()
        details = {"name":name, "phone":phone,"city":city}
        contacts.append(details)
        print(f"{name.capitalize()} added!")
    elif option == "2":
        if not contacts:
            print("No contacts yet. Add some first!")
        else:
            print("====== All Contacts ======")
            for index,contact in enumerate(contacts,start=1):
                print(f"{index}. {contact["name"].capitalize()} - {contact["phone"]} - {contact["city"].capitalize()}")
    elif option == "3":
        search_name = input("Enter name you want to search : ").lower().strip()
        found = False
        for contact in contacts:
            if contact["name"].lower() == search_name:
                print(contact)
                found = True
                break
        if not found:
            print(f"No contact named '{search_name}' found.")
    elif option == "4":
        if not contacts:
            print("No contacts yet. Add some first!")
        else:
            search_name = input("Enter name of your contact whose details you need to modify: ").lower().strip()
            found = False
            for contact in contacts:
                if contact["name"].lower() == search_name:
                    new_phone = input("Enter new phone number: ").strip()
                    contact["phone"] = new_phone
                    print(f"phone number updated for {contact['name'].capitalize()}")
                    found = True
                    break
            if not found:
                print(f"No contact named '{search_name}' found.")
    elif option == "5":
        if not contacts:
            print("No contacts yet. Add some first!")
        else:
            search_name = input("Enter name of contact to delete: ").strip().lower()
            found = False
            for contact in contacts:
                if contact["name"].lower() == search_name:
                    found = True
                    confirm = input(f"Are you sure you want to delete {contact['name'].capitalize()}? (y/n): ").strip().lower()    
                    if confirm in ["y", "yes"]:
                        contacts.remove(contact)
                        print(f"{search_name.capitalize()} deleted successfully!")
                    else:
                        print("Deletion cancelled.")
                    break    # stop searching
            if not found:
                print(f"No contact named '{search_name}' found.")
    elif option == "6":
        print("Goodbye!")
        break
    else:
        print(f"'{option}' is not a valid option. Please choose 1-6.")