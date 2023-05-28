# Example 1

class ExampleClass:
    pass


# Example 2

class Person:
    name = None


alice = Person()
bob = Person()

alice.name = 'Alice'

# print(Person.name)
# print(bob.name)
# print(alice.name)
#
#
# print(bob is alice) # False
# print(bob is Person) # False
# print(alice is Person) # False


# Examples 3

# print(Person.__dict__)
# print(bob.__dict__)
# print(alice.__dict__)


# Examples 4

class Math:
    def add(x, y):
        return x + y


print(Math.add(2, 3))


# Example 5

class Person2:
    name = 'Noname'
    def greet(self):
        return 'Hello, ' + self.name + '!'


print(Person2().greet())

alice = Person2()
alice.name = 'Alice'

print(alice.greet())
