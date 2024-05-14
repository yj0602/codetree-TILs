class User:
    def __init__(self, username, level):
        self.username = username
        self.level = level

user1 = User("codetree", 10)

username, level = input().split()
user2 = User(username, int(level))

print("user {} lv {}".format(user1.username, user1.level))
print("user {} lv {}".format(user2.username, user2.level))