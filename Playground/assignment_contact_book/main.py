contacts = {}

def add_contact():
    print('\n1. Adding a contact to the contact book')
    add_name = input('\nPlease enter the contact name: ')
    add_number_str = input('\nPlease enter the phone number: ')
    add_number_int = int(add_number_str)
    contacts[add_name] = add_number_int
    print('\nContact added to the contacts book.')


def search_contact():
    print('\n2. Searching a contact in the contact book')
    search_name = input('\nEnter contact name: ')
    if search_name in contacts:
        print('\nContact entry for\nName:', search_name, ', Number:', contacts[search_name])
    else:
        print('Contact not found. Returning to main menu')
    

def delete_contact():
    print('\n3. Deleting a contact')
    delete_name = input('\nEnter contact name: ')
    if delete_name in contacts:
        print('\nDelete contact entry for\nName:', delete_name, ', Number:', contacts[delete_name], '?')
        confirmation = input('\nEnter Yes or No: ')
        if confirmation == 'Yes':
            del contacts[delete_name]
            print('Contact deleted.')
        elif confirmation == 'No':
            print('No contacts deleted.')

def list_contacts():
    print('\n4. Viewing all contacts')
    for name,number in sorted(contacts.items()):
        print('\nList of contacts:')
        print(name, number)


def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. View All Contacts")
        print("5. Exit")

        choice = input("Enter your choice as a number: ")
        valid_choices = ['1', '2', '3', '4', '5']


        if choice not in valid_choices:
            print('\nThat is not a valid choice')
            continue
        elif choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            list_contacts()
        elif choice == '5':
            print('Closing Contact Book')
            break

main()