# # Example 1
#
# class ExampleClass:
#     pass
#
#
# # Example 2
#
# class Person:
#     name = None
#     last_name = None
#
#
# alice = Person()
# bob = Person()
#
# print(Person.__dict__)
# print(alice.__dict__)
# alice.name = 'Alice'
#
# print(alice.name)

# Examples 3

# print(Person.__dict__)
# print(bob.__dict__)
# print(alice.__dict__)


# Examples 4

# class Math:
#     def add(x, y):
#         return x + y
#
#
# print(Math.add(2, 3))
#
#
# # Example 5
#

class Person2:
    name = 'Noname'

    def greet(self):
        return 'Hello, ' + self.name + '!'

    def go(self):
        pass


# print(Person2().greet())

alice = Person2()
alice.name = 'Alice'
bob = Person2()

print(alice.greet())

print(len(alice))
