print("CONTACT BOOK")

contacts = {}

while True:
    print("\n1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone
        print("Contact added.")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\nYour contacts:")

            for name, phone in contacts.items():
                print(name, "-", phone)

    elif choice == "3":
        name = input("Enter name to search: ")

        if name in contacts:
            print("Phone number:", contacts[name])
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Please choose a valid option.")

