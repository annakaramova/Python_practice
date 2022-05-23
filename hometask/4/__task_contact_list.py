# Write a simple contact list
# On start program should print available list of commands (example below)
# 1. Add contact
# 2. Find contact
# 3. Print all
# 4. Exit
#
# By selecting 1. program asks for contact info to add
# Name
# Phone number
#
# On successful save it should print - New contact has been added
#
# By selecting 2. Program asks for search term. If list of contacts contains required data it should print it to the
# console (example below)
# 1. Ivan - 034567678
# 2. Petr - 345434534
#
# By selecting 3. Program prints a list of all saved contacts to the
# console (example below)
# 1. Ivan - 034567678
# 2. Petr - 345434534
#
# By selecting 4. Program exit

from enum import Enum


class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Action(Enum):
    addContact = 1
    findContact = 2
    printAll = 3
    exit = 4


class App:
    def __init__(self):
        self.persons = []

    def process_command_line(self):
        while True:
            self.print_usage()
            action = Action(int(input()))
            if action == Action.addContact:
                self.add_contact()
            elif action == Action.findContact:
                print("Contact:", end='')
                result = self.find_contact(input())
                print("Found:")
                self.print_list(result)
            elif action == Action.printAll:
                self.print_all()
            elif action == Action.exit:
                break

    def add_contact(self):
        print("Name:", end='')
        name = input()
        print("Phone number:", end='')
        phone_number = input()
        person = Person(name, phone_number)
        self.persons.append(person)

    def find_contact(self, search_term: str):
        return [person for person in self.persons if search_term in person.phone or search_term in person.name]

    def print_all(self):
        self.print_list(self.persons)

    @staticmethod
    def print_list(lst):
        for item in lst:
            print(f"{item.name} - {item.phone}")

    @staticmethod
    def print_usage():
        print("1. Add contact")
        print("2. Find contact")
        print("3. Print all")
        print("4. Exit")


App().process_command_line()

