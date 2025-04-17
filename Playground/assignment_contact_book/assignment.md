# Python Assignment: Simple Contact Book

## Problem Statement:
Create a simple contact book program that allows the user to:

1. Add new contacts (name and phone number)

2. Search for a contact by name

3. Delete a contact

4. View all contacts

5. Exit the program

## Features to Implement:
Use a dictionary to store the contacts, with names as keys and phone numbers as values.

Display a menu that repeats until the user chooses to exit:

```
1. Add Contact
2. Search Contact
3. Delete Contact
4. View All Contacts
5. Exit
```

Perform actions based on the user’s choice using if-elif-else or match-case (if she’s seen it).

Use functions for each menu option to keep the code organized.


## Example
```python

contacts = {}


add_contact():
    # add contact
    name = input("Enter name: ")
    phone = input("Enter phone number: ")


while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_contact()
```
## Bonus
Save the contacts dictionary into a file using json so it can be loaded next time.
