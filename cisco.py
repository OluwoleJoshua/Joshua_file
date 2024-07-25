# class Car:
#     def __init__(self):
#         self.brand = 'Toyota'
#         self.colour = 'Blue'
#
#     def move(self):
#         print(f"my {self.brand} is moving")
#
#
# my_car = Car()
# my_car.move()
#
#
# class MyCar:
#     def __init__(self, name, model, color):
#         self.name = name
#         self.model = model
#         self.color = color
#
#
# tesla = MyCar('Tesla','Model-Y', 'White')
# benz = MyCar('Benz', 'C-Class', 'Pink')
# toyota = MyCar('Toyota', 'Camry', 'blue')
# print(toyota.model, toyota.name, toyota.color)
#
class Person:
    def __init__(self, fname, lname, age):
        self.firstname = fname
        self.lastname = lname
        self.age = age

    def xtics(self):
        print(self.firstname, self.lastname, self.age)


# x = Person()
# x.xtics()


class Student(Person):
    def __init__(self, golf, ace, age, year):
        # Person.__init__(self, golf, ace, age)
        super().__init__(golf, ace, age)
        self.graduation = year

    def welcome(self):
        print(f"Welcome, {self.firstname}, {self.lastname} class of {self.graduation} to your graduation")


x = Student('Ayo', 'aisha', 20, 2024)
x.welcome()
