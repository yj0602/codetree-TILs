class Person:
    def __init__(self, name, address, city):
        self.name = name
        self.address = address
        self.city = city

n = int(input())
people = []
for _ in range(n):
    name, address, city = input().split()
    people.append(Person(name, address, city))

slowest_person = max(people, key=lambda x: x.name)

print('name', slowest_person.name)
print('addr', slowest_person.address)
print('city', slowest_person.city)