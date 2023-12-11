# 1
#import random
#
# class MusicAlbum:
# def __init__(self, title, artist, release_year, genre, tracklist):
# self.title = title
# self.artist = artist
# self.release_year = release_year
# self.genre = genre
# self.tracklist = tracklist
# def play_random_track(self):
# if self.tracklist:
# random_track = random.choice(self.tracklist)
# print("Случайный трек:", random_track)
# else:
# print("Альбом не содержит треков.")
# 2
# class Student:
# def __init__(self, name, age, grade, scores):
# self.name = name
# self.age = age
# self.grade = grade
# self.scores = scores
#
# def average_score(self):
# if self.scores:
# return sum(self.scores) / len(self.scores)
# else:
# return 0
# 3
# class Recipe:
# def __init__(self, name, ingredients):
# self.name = name
# self.ingredients = ingredients
#
# def print_ingredients(self):
# print(f"Ингредиенты для рецепта '{self.name}':")
# for ingredient in self.ingredients:
# print(ingredient)
#
# def cook(self):
# print(f"Готовим блюдо: {self.name}")
# print(f"{self.name} готово! Приятного аппетита!")
#
# spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])
#
# spaghetti.print_ingredients()
#
# spaghetti.cook()
#
# cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])
#
# cake.print_ingredients()
#
# cake.cook()
# 4
# class Publisher:
# def __init__(self, name, location):
# self.name = name
# self.location = location
# def get_info(self):
# return f"Издательство: {self.name}, Расположение: {self.location}"
# def publish(self, message):
# print(message)
# class BookPublisher(Publisher):
# def __init__(self, name, location, num_authors):
# super().__init__(name, location)
# self.num_authors = num_authors
# def get_info(self):
# return f"Издательство книг: {self.name}, Расположение: {self.location}, Количество авторов: {self.num_authors}"
# class NewspaperPublisher(Publisher):
# def __init__(self, name, location, num_pages):
# super().__init__(name, location)
# self.num_pages = num_pages
# def get_info(self):
# return f"Газетное издательство: {self.name}, Расположение: {self.location}, Количество страниц: {self.num_pages}"
# 5
# class BankAccount:
# def __init__(self, balance, interest_rate):
# self.__balance = balance
# self.__interest_rate = interest_rate
# self.__transactions = []
#
# def deposit(self, amount):
# if amount > 0:
# self.__balance += amount
# self.__transactions.append(f"Депозит: +{amount}")
# else:
# print("Сумма для депозита должна быть положительной.")
#
# def withdraw(self, amount):
# if amount > 0 and amount <= self.__balance:
# self.__balance -= amount
# self.__transactions.append(f"Снятие: -{amount}")
# elif amount <= 0:
# print("Сумма для снятия должна быть положительной.")
# else:
# print("Недостаточно средств на счете.")
#
# def add_interest(self):
# interest = self.__balance * self.__interest_rate
# self.__balance += interest
# self.__transactions.append(f"Начисление процентов: +{interest}")
#
# def history(self):
# for transaction in self.__transactions:
# print(transaction)
#
# account = BankAccount(100000, 0.05)
#
# account.deposit(15000)
#
# account.withdraw(7500)
#
# account.add_interest()
#
# account.history()
# 6
# class Employee:
# def __init__(self, name, age, salary):
# self.__name = name
# self.__age = age
# self.__salary = salary
# self.__bonus = 0
#
# def get_name(self):
# return self.__name
#
# def get_age(self):
# return self.__age
#
# def get_salary(self):
# return self.__salary
#
# def set_bonus(self, bonus):
# self.__bonus = bonus
#
# def get_bonus(self):
# return self.__bonus
#
# def get_total_salary(self):
# return self.__salary + self.__bonus
#
#
# employee = Employee("Марина Арефьева", 30, 90000)
#
# employee.set_bonus(15000)
#
# print("Имя:", employee.get_name())
# print("Возраст:", employee.get_age())
# print("Зарплата:", employee.get_salary())
# print("Бонус:", employee.get_bonus())
# print("Итого начислено:", employee.get_total_salary())
# 7
# class Animal:
# def __init__(self, name, species, legs):
# self.name = name
# self.species = species
# self.legs = legs
#
# def voice(self):
# print(f"{self.name} the {self.species} makes a sound.")
#
# def move(self):
# print(f"{self.name} the {self.species} is moving.")
#
# class Dog(Animal):
# def __init__(self, name, breed, legs):
# super().__init__(name, "dog", legs)
# self.breed = breed
#
# def bark(self):
# print(f"{self.name} the {self.breed} dog barks.")
#
# class Bird(Animal):
# def __init__(self, name, species, legs, wingspan):
# super().__init__(name, species, legs)
# self.wingspan = wingspan
#
# def fly(self):
# print(f"{self.name} the {self.species} with a wingspan of {self.wingspan} is flying.")
#
# dog = Dog("Геральт", "доберман", 4)
# bird = Bird("Вася", "попугай", 2)
#
# dog.voice()
# bird.voice()
# dog.move()
# bird.move()
# dog.bark()
# bird.fly()
# 8
# class Shape:
# def __init__(self, name, color):
# self.name = name
# self.color = color
#
# def describe(self):
# print(f"Это {self.color} {self.name}.")
#
#
# class Circle(Shape):
# def __init__(self, color, radius):
# super().__init__("окружность", color)
# self.radius = radius
#
# def area(self):
# return 3.14159265359 * self.radius ** 2
#
#
# class Rectangle(Shape):
# def __init__(self, color, length, width):
# super().__init__("прямоугольник", color)
# self.length = length
# self.width = width
#
# def area(self):
# return self.length * self.width
#
#
# class Triangle(Shape):
# def __init__(self, color, base, height):
# super().__init__("треугольник", color)
# self.base = base
# self.height = height
#
# def area(self):
# return 0.5 * self.base * self.height
#
#
# circle = Circle("красный", 5)
# rectangle = Rectangle("синий", 3, 4)
# triangle = Triangle("фиолетовый", 6, 8)
#
# circle.describe()
# rectangle.describe()
# triangle.describe()
#
# print(f"Площадь треугольника {triangle.area()}, окружности {circle.area()}, прямоугольника {rectangle.area()} см.")
# 9
# class Candy:
# def __init__(self, name, price, weight):
# self.name = name
# self.price = price
# self.weight = weight
#
# class Chocolate(Candy):
# def __init__(self, name, price, weight, cocoa_percentage, chocolate_type):
# super().__init__(name, price, weight)
# self.cocoa_percentage = cocoa_percentage
# self.chocolate_type = chocolate_type
#
# class Gummy(Candy):
# def __init__(self, name, price, weight, flavor, shape):
# super().__init__(name, price, weight)
# self.flavor = flavor
# self.shape = shape
#
# class HardCandy(Candy):
# def __init__(self, name, price, weight, flavor, filled):
# super().__init__(name, price, weight)
# self.flavor = flavor
# self.filled = filled
#
# chocolate = Chocolate(name="Швейцарские луга", price=325.50, weight=220, cocoa_percentage=40, chocolate_type="молочный")
# gummy = Gummy(name="Жуй-жуй", price=76.50, weight=50, flavor="вишня", shape="медведь")
# hard_candy = HardCandy(name="Crazy Фрукт", price=35.50, weight=25, flavor="манго", filled=True)
#
# print("Шоколадные конфеты:")
# print(f"Название конфет: {chocolate.name}")
# print(f"Стоимость: {chocolate.price} руб")
# print(f"Вес брутто: {chocolate.weight} г")
# print(f"Процент содержания какао: {chocolate.cocoa_percentage}")
# print(f"Тип шоколада: {chocolate.chocolate_type}")
# print("\nМармелад жевательный:")
# print(f"Название конфет: {gummy.name}")
# print(f"Стоимость: {gummy.price} руб")
# print(f"Вес брутто: {gummy.weight} г")
# print(f"Вкус: {gummy.flavor}")
# print(f"Форма: {gummy.shape}")
# print("\nФруктовые леденцы:")
# print(f"Название конфет: {hard_candy.name}")
# print(f"Стоимость: {hard_candy.price} руб")
# print(f"Вес брутто: {hard_candy.weight} г")
# print(f"Вкус: {hard_candy.flavor}")
# print(f"Начинка: {hard_candy.filled}")
# 10
# class Soldier:
# def __init__(self, name, rank, service_number):
# self.name = name
# self.__rank = rank  # Приватное свойство для воинского звания
# self.__service_number = service_number  # Приватное свойство для порядкового номера
#
# def get_rank(self):
# return self.__rank
#
# def confirm_service_number(self, service_number):
# return self.__service_number == service_number
#
# def promote(self):
# if self.__rank == "рядовой":
# self.__rank = "сержант"
# return True
# else:
# return False
#
# def demote(self):
# if self.__rank == "сержант":
# self.__rank = "рядовой"
# return True
# else:
# return False
#
# soldier1 = Soldier("Иван Сусанин", "рядовой", "12345")
#
# print("Воинское звание:", soldier1.get_rank())
#
# service_number = "12345"
# if soldier1.confirm_service_number(service_number):
# print(f"Порядковый номер {service_number} подтвержден.")
# else:
# print(f"Порядковый номер {service_number} не подтвержден.")
#
# if soldier1.promote():
# print("Солдат повышен в звании:", soldier1.get_rank())
# else:
# print("Солдат не может быть повышен в звании.")
#
# if soldier1.demote():
# print("Солдат понижен в звании:", soldier1.get_rank())
# else:
# print("Солдат не может быть понижен в звании.")