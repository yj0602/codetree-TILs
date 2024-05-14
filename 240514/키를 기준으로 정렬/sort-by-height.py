n = int(input())

class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

people = [
    Person("lee", 167, 40),
    Person("kim", 149, 32),
    Person("park", 161, 53),
    Person("choi", 183, 70),
    Person("jung", 155, 45)
]

people.sort(key=lambda person: person.height)

for person in people:
    print(person.name, person.height, person.weight)