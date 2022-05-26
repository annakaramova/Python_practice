# Write a program that will find a couple.
# On the start program have to create a list of 10 random people male and female.
# Every person have three fields name, age, sex
# Program asks a user to enter a name and a desired age for search
# Matching rule
# Couple can match if users age difference not more than 5 years and both names has at least same two letters
# If match is found program should print - Congrats there is a matching pair Name1 + Name2!
# It no match - just print Sorry, no match! =(

import random


class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    @staticmethod
    def make_man():
        man_names = ['Mark', 'Alex', 'Peter', 'Simon', 'Andrey', 'Joseph', 'Noah', 'Frank', 'Dilan', 'Brandon',
                     'Joey', 'Chandler', 'Ross']
        name = random.choice(man_names)
        age = random.randint(18, 49)
        return Person(name, age, "male")

    @staticmethod
    def make_woman():
        woman_names = ['Marta', 'Alexa', 'Penelopa', 'Simona', 'Andrea', 'Jennie', 'Nelly', 'Frida', 'Donna', 'Brenda',
                       'Sarah', 'Monica', 'Rachel']
        name = random.choice(woman_names)
        age = random.randint(18, 49)
        return Person(name, age, "female")


class Matcher:
    def __init__(self):
        self.people = []
        for i in range(10):
            if random.randint(1, 2) == 1:
                self.people.append(Person.make_woman())
            else:
                self.people.append(Person.make_man())

    def search(self, name, age):
        return [person
                for person in self.people
                if abs(person.age - age) <= 5 and person.name[:2] == name[:2]
                ]

    def process(self):
        print('Your name: ', end='')
        name = input()
        print('Desired age: ', end='')
        age = int(input())
        results = self.search(name, age)
        if len(results) > 0:
            first_match = results[0]
            print(f"Congrats there is a matching pair: {name} + {first_match.name}!")
        else:
            print('Sorry, no match!')


Matcher().process()
