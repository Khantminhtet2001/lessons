import math

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be a non-negative number.")
        self._radius = value

    def area(self):
        return math.pi * self._radius * self._radius

    def circumference(self):
        return 2 * math.pi * self._radius


# Create a circle object with a radius of 5
circle = Circle(5)

# Modify the radius attribute
circle.radius = 10

# Calculate and print the area and circumference of the circle
area = circle.area()
circumference = circle.circumference()
print(f"The area of the circle is {area} and the circumference is {circumference}")