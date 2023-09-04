
class User: # Таблица
    pass


# SELECT * FROM user;

user = User()

user1 = User.objects.filter(id=2)
user2 = User.objects.get(id=2)

result1 = ['User2']
print(result1[0].email)
result2 = 'User2'
result2.email