
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        return self.name + ' ' + self.surname

tom = Person('Thomas', 'Smith')


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        return self.name + ' ' + self.surname

    # сеттер для свойства full_name
    @full_name.setter
    def full_name(self, new):
        self.name, self.surname = new.split(' ')



tom = Person('Thomas', 'Smith')
print(tom.full_name)
tom.full_name = 'Alice Cooper'
print(tom.name)
print(tom.surname)
print(tom.full_name)
