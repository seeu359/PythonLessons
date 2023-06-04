# # Example 1
#
# class Person(object):
#
#     def __init__(self, name, surname):
#         self.full_name = name + surname
#
#
# bob = Person('Bob', 'Hello')


# Example 2

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def __len__(self):
#         return 10000000
#
# tom = Person('Thomaeqewrs')
#
# print(len(tom))

# Протокол обращения по индексам

class PersonIndex:

    def __init__(self, name):
        self.name = name

    def __getitem__(self, item):
        raise Exception('Нельзя обращаться по индексу')



new_bob = PersonIndex('Bob')

print(new_bob[1])
print(len)