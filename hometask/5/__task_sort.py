# Write a program that will create a list of people with name, age, height, and weight
# Sort the list of people by age
import random


class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    @staticmethod
    def make_person():
        people_names = ['Mark', 'Alex', 'Peter', 'Simona', 'Andrey', 'Joseph', 'Noah', 'Frank', 'Dilan', 'Brandon',
                        'Joey', 'Charley', 'Ross', 'Monica', 'Rachel']
        name = random.choice(people_names)
        age = random.randint(18, 79)
        height = random.randint(145, 215)
        weight = random.randint(45, 299)
        return Person(name, age, height, weight)


class Sorter:
    def __init__(self):
        self.people = []
        for i in range(10):
            self.people.append(Person.make_person())

    def sort(self):
        return sorted(self.people, key=lambda person: person.age)


sorter = Sorter()
sorted_people = sorter.sort()
print("Name\t\t\tAge\t\t\tHeight\t\tWeight")
print("-" * 46)
for person in sorted_people:
    print(person.name, person.age, person.height, person.weight, sep='\t\t\t')
