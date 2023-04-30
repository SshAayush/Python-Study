class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0
    
    def follow(self,user):
        user.followers += 1
        self.following += 1

user_1 = User(10, "Aayush")
user_2 = User(20, "Hesoyam")

# user_1.id = 10
# user_1.name = "Aayush"

# user_2.id = 20
# user_2.name = "Hesoyam"

user_1.follow(user_2)

print(user_1.following , user_1.followers)
print(user_2.following , user_2.followers)