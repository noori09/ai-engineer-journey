# Contact Book CLI v2
# Refactored using functions (Day 5)
# Same features as v1 but organized into reusable functions

contact_menu = {
    "1": "Add a contact",
    "2": "List all contacts",
    "3": "Search for a contact",
    "4": "Update a contact's phone",
    "5": "Delete a contact",
    "6": "Quit",
}

contacts = []


def show_menu():
    print("\n Contact Menu")
    for key, value in contact_menu.items():
        print(f"{key}. {value}")


def format_contact(contact):
    return f"{contact['name'].capitalize()} - {contact['phone']} - {contact['city'].capitalize()}"


def list_contacts(contacts):
    if not contacts:
        print("No contacts yet. Add some first!")
    else:
        print("====== All Contacts ======")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. {format_contact(contact)}")


def find_contact(contacts, name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None


def search_contact(contacts):
    if not contacts:
        print("No contacts yet.")
        return
    name = input("Enter name you want to search: ").strip()
    result = find_contact(contacts, name)
    if result is None:
        print(f"No contact named '{name}' found")
    else:
        print(f"found {format_contact(result)} ")


def add_contact(contacts):
    name = input("Enter contact's Name: ").strip()
    phone = input("Enter contact's Mobile Number: ").strip()
    city = input("Enter contact's City: ").strip()
    contacts.append({"name": name, "phone": phone, "city": city})
    print(f"{name.capitalize()} added!")


def update_contact(contacts):
    if not contacts:
        print("No contacts yet. Add some first!")
        return
    name = input("Enter name you want to update: ").strip()
    contact = find_contact(contacts, name)
    if contact is None:
        print(f"No contact named '{name}' found")
        return
    new_phone = input("Enter new phone number: ").strip()
    contact["phone"] = new_phone
    print(f"Phone number updated for {contact['name'].capitalize()}")


def delete_contact(contacts):
    if not contacts:
        print("No contacts yet. Add some first!")
        return
    name = input("Enter name you want to delete: ").strip()
    contact = find_contact(contacts, name)
    if contact is None:
        print(f"No contact named '{name}' found")
        return
    confirm = (
        input(
            f"Are you sure you want to delete {contact['name'].capitalize()}? (y/n): "
        )
        .strip()
        .lower()
    )
    if confirm in ["y", "yes"]:
        contacts.remove(contact)
        print(f"{name.capitalize()} deleted successfully!")
    else:
        print("Deletion cancelled.")


def main():
    while True:
        show_menu()
        option = input("\nChoose an option (1-6): ").strip()

        if option == "1":
            add_contact(contacts)
        elif option == "2":
            list_contacts(contacts)
        elif option == "3":
            search_contact(contacts)
        elif option == "4":
            update_contact(contacts)
        elif option == "5":
            delete_contact(contacts)
        elif option == "6":
            print("Goodbye!")
            break
        else:
            print(f"'{option}' is not a valid option. Please choose 1-6.")


main()
