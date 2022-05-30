from Person import Person
from Action import Action
from Validator import Validator
from tabulate import tabulate

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
        phone_number = Validator.input_phone_number()
        email = Validator.input_email()
        person = Person(name, phone_number, email)
        self.persons.append(person)

    def find_contact(self, search_term: str):
        return [person
                for person in self.persons
                if search_term in person.phone or search_term in person.name or search_term in person.email
                ]

    def print_all(self):
        self.print_list(self.persons)

    @staticmethod
    def print_list(lst):
        print(tabulate([[person.name, person.phone, person.email] for person in lst], headers=["Name", "Phone", "Email"]))

    @staticmethod
    def print_usage():
        print("1. Add contact")
        print("2. Find contact")
        print("3. Print all")
        print("4. Exit")