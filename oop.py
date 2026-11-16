from abc import ABC, abstractmethod

'''Инкапсуляция'''

class Person:
    def __init__(self, age):
         self.__age = 0
    
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            raise ValueError('Возраст не может быть отрицательным')

    def get_age(self):
        return self.__age

p = Person()
p.set_age(25)
print(p.get_age())
p.set_age(-5)
print(p.get_age())


'''Наследование'''

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return 'I am Animal'
    
class Dog(Animal):
    def speak(self):
        return 'Woof'

class Cat(Animal):
    def speak(self):
        return 'Meow'

dog = Dog('Buddy')
cat = Cat('Kitty')
print(dog.name, dog.speak())
print(cat.name, cat.speak())


'''Полиморфизм'''

class Vehicle:
    def move(self):
        return 'Vehicle is mooving'

class Car(Vehicle):
    def move(self):
        return 'Car is driving'

class Bicycle(Vehicle):
    def move(self):
        return 'Bicycle is pedaling'

car = Car()
bike = Bicycle()
print(car.move())
print(bike.move())



'''Абстракция'''

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


rect = Rectangle(10, 5)
circ = Circle(7)

print(rect.area())
print(circ.area())