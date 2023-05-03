# creating our first class
class Instagram():
    """Instagram class, stores username , ID, Followers"""

    # class Constructor or init function
    def __init__(self, id, name):
        """Class Constructor or init function"""
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        """To allow user's to follow each other"""
        user.followers += 1
        self.following += 1

    def display(self):
        print(
            f"Name: {self.name},ID: {self.id},Followers: {self.followers},Following: {self.following}")


# assigning objects to class and creating new user
user_1 = Instagram("001", "Yash")
user_2 = Instagram("002", "Joshi")

# following each other
user_1.follow(user_2)
user_2.follow(user_2)

# checking the new follower / following count
user_1.display()
user_2.display()
