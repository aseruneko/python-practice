class User:
    def __init__(self, name):
        # instance variable
        self.name = name

tom = User("tom")
bob = User("bob")

print(tom.name)
print(bob.name)