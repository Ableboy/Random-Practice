class Dog:
    # class for instances of a dog
    def __int__(self, name, movement, breed):
        self.name = name
        self.movement = movement
        self.breed = breed
    def describe_object(self):
        print(f"your pet {self.name} is great!")
        print(f"{self.name} loves {self.movement} around.")
        print(f"{self.name} is {self.breed} in nature")

my_dog = Dog("lucy", "walking", "reddish")
my_dog.describe_object()
print(f"your pet {my_dog.name} is great!")
print(f"{my_dog.name} loves {my_dog.movement} around.")
print(f"{my_dog.name} is {my_dog.breed} in nature")
