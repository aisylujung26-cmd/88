class Fruit:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


fruit1 = Fruit("apple", 10)
fruit2 = Fruit("banana", 20)

print(fruit2.name, fruit2.weight)
print(fruit1.name, fruit1.weight)

fruit1.weight = 40
print(fruit1.name, fruit1.weight)


class Fruit:
    def __init__(self, name, days_ripe):
        self.name = name
        self.days_ripe = days_ripe

    def describe(self):
        print(f"This id a {self.name} ")

    def wait_a_day(self):
        self.days_ripe -= 1
        print(f"{self.name} day ripe: {self.days_ripe} ")

    def is_ripe(self):
        return self.days_ripe <= 0


apple = Fruit("apple", 2)
apple.describe()
apple.wait_a_day()
print(apple.is_ripe())
apple.wait_a_day()
print(apple.is_ripe())


class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2


c1 = Circle(2)
c2 = Circle(5)

print(c1.area())
print(c2.area())

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def __str__(self):
        return f"Owner: {self.owner}, Balance: {self.__balance}"

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit {amount}. Balance:  {self.__balance}")
        else:
            print("Deposit can't be negative")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Not enough money on your account")
        else:
            self.__balance -= amount
            print(f"Withdraw {amount}. Balance:  {self.__balance}")

    def get_balance(self):
        return self.__balance

account = BankAccount("John", 100)
print(account)
account.deposit(100)
print(account)
account.withdraw(250)
account.withdraw(200)
print(account.get_balance())


class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating ")
    def make_sound(self):
        print(f"{self.name} makes a sound ")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says: Woof!")

    def swim(self):
        print(f"{self.name} swims around")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says: Meow!")

    def play(self):
        print(f"A {self.name} can play with ball ")

dog = Dog("Doggi")
cat = Cat("Sima")
dog.eat()
dog.make_sound()
cat.make_sound()
dog.swim()
cat.play()
cat.eat()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks
    def __str__(self):
        return (f"Name: {self.name}, "
                f"Age: {self.age}, Marks: {self.marks}")
student = Student("John", 30, 100)
print(student)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return f"Rectangle width: {self.width}, height: {self.height}"

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

rectangle = Rectangle(10, 20)
print(rectangle)
print(rectangle.perimeter())
print(rectangle.area())

class Thermometer:
    def __init__(self):
        self.__temperature = -273

    def set_temperature(self, t):
        if t >= -273:
            self.__temperature = t
        else:
            print("Temperature out of range")

    def get_temperature(self):
        return self.__temperature

term = Thermometer()
print(term.get_temperature())
term.set_temperature(15)

print(term.get_temperature())






