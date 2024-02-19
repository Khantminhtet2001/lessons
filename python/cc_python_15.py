# name="Khant Min Htet"
# print(name.upper())

class Car :
    sterringWheel=1
    def __init__(self,name,wheels):
        self.name=name
        self.wheels=wheels
        
    def drive(self) :
        print(f'{self.name} is driving')
        print(f'{self.wheels} wheels')

    #class lavel method
    @classmethod
    def common(cls):
        print(f'all car has only {cls.sterringWheel} sterring wheel')

# lambo=Car("lamborghini",4)
# lambo.drive()

# maecedes=Car('marcedes',4)
# maecedes.drive()

# print(lambo.name)
# print(lambo.wheels)
        
print(Car.sterringWheel)
Car.common()
