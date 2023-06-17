class Car:
    def __init__(self, model):
        self.__model = model


toyota = Car('Toyota')


class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        return self.name + ' ' + self.surname

    # сеттер для свойства full_name
    @full_name.setter
    def full_name(self, new_brand):
        self.name, self.surname = new.split(' ')

tom = Person('Thomas', 'Smith')
print(tom)
tom.full_name = 'Toyota'

# print(tom.name)
# print(tom.surname)
# print(tom.full_name)
#
# import random
#
# a = ['1', '2', '3']
#
#
# print(random.choice(a))
