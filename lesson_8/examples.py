some_list = [1, 2, 'hi']
print(some_list)

some_list[-1] = 200
print(some_list)


some_list = [1, 2, 'hello', '1123']
print(some_list[1:3])

some_list[1:3] = [10, 20]
print(some_list)

#####

a = [1, 2, 3]

b = a

print(id(a))
print(id(b))

c = [1, 2, 3]


##########################


a = [1]
b = a
print(b)

#######

a = []
l = [a, a]
a.append(1)
print(l)


######

a = []
pair = (a, a)
pair[0].append(1)
pair[1].append(2)
print(pair)


########

some_list1 = ['world', 'hello', 'some_str']

for i in enumerate(some_list1):
    print(i)


## либо так

for index, value in enumerate(some_list1):
    print(index)
    print(value)
