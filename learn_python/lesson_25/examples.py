# Example 1

class Person:

    def __init__(self, name):
        self.name = name


bob = Person('Bob')
# alice = Person()


## Example 2

class Person:
    def __init__(self, name):
        self.name = name
    def __len__(self):
        return len(self.name)

tom = Person('Thomas')
len(tom)

# Протокол обращения по индексам

class PersonIndex:

    def __init__(self, name):
        self.name = name

    def __getitem__(self, item):
        return self.name[2]


new_bob = PersonIndex('Bob')
print(new_bob[0])