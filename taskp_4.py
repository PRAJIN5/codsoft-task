contacts = {}

def add_contact():
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print(f"Contact '{name}' already exists.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
    print(f"Contact '{name}' added successfully.")

def view_contacts():
    if contacts:
        print("\nYour contacts:")
        for name, details in contacts.items():
            print(f"{name}: Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}")
    else:
        print("No contacts found.")

def search_contact():
    name = input("Enter the contact name to search: ").strip()
    if name in contacts:
        details = contacts[name]
        print(f"\nFound contact for {name}: Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}")
    else:
        print(f"No contact found for '{name}'.")

def update_contact():
    name = input("Enter the name of the contact to update: ").strip()
    if name in contacts:
        print("What would you like to update?")
        print("1. Phone")
        print("2. Email")
        print("3. Address")
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            phone = input("Enter new phone number: ").strip()
            contacts[name]['Phone'] = phone
            print(f"Phone number for '{name}' updated.")
        elif choice == '2':
            email = input("Enter new email: ").strip()
            contacts[name]['Email'] = email
            print(f"Email for '{name}' updated.")
        elif choice == '3':
            address = input("Enter new address: ").strip()
            contacts[name]['Address'] = address
            print(f"Address for '{name}' updated.")
        else:
            print("Invalid choice.")
    else:
        print(f"No contact found for '{name}'.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"No contact found for '{name}'.")

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the contact book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
