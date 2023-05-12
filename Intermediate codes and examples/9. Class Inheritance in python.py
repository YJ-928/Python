class Animal:

    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

# to make our fish class Inherit properties of Animal Class
# declare it as shown below and
# define a super Contructor


class Fish(Animal):

    def __init__(self):
        super().__init__()

    def swim(self):
        print("Move in water.")

    def breathe(self):
        """To modify a function from the super class"""
        super().breathe()
        print("doing this under water")


nemo = Fish()
nemo.swim()
nemo.breathe()  # properties of animal class, but can be accessed due to inheritance
print(nemo.eyes)

# checkout the diffrence of the two breathe functions
dog = Animal()
dog.breathe()
