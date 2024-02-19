class Dog:
    def __init__(self, name, breed):
        self._name = name
        self._breed = breed

    @property
    def name(self):
        return self._name

    @property
    def breed(self):
        return self._breed

    @name.setter
    def name(self, value):
        self._name = value

    @breed.setter
    def breed(self, value):
        self._breed = value


# Create two instances of the "Dog" class
dog1 = Dog("Fido", "Golden Retriever")
dog2 = Dog("Max", "Labrador")

# Set the attributes of the instances using the setter methods
dog1.name = "Buddy"
dog1.breed = "Boxer"
dog2.name = "Bella"
dog2.breed = "Beagle"

# Print the updated values of the attributes
print(f"Dog1's name is {dog1.name} and breed is {dog1.breed}")
print(f"Dog2's name is {dog2.name} and breed is {dog2.breed}")