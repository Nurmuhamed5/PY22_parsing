# ООП(обьектно-ориентированное программирование) - цель создания была связать обьекта с ее данными

# Класс - это описание того, какими свойствами (данными) и поведением должен обладать обьект(экзампляр)

# Обьект - это экземпляр  собственным состоянием этих свойств.

# Свойствами называют обычные переменные (name='John', height=185)

# Поведение это обычные функции(def eat - методы)

"======================"

# kirk = ['James Kirk', 34, 'captain', 2000]
# snow = ['John Snow', 28, 'Police oficier', 1500]
# mccoy = ['Leonard McCoy', 'chief', 1700]

# class Human():
#     def __init__(self, name, age, job, salary):
#         self.name = name
#         self.age = age
#         self.job = job
#         self.salary = salary

#     def show_info(self):
#         return f'Name: {self.name}, \nAge: {self.age}, \nJob: {self.job}, \nSalary: {self.salary}.\n'

# kirk = Human('James Kirk', 34, 'captain', 2000)
# snow = Human('John Snow', 28, 'Police oficier', 1500)
# mccoy = Human('Leonard McCoy', 25, 'chief', 1700)

# print(kirk.show_info())
# print(snow.show_info())
# print(mccoy.show_info())

# class Dog():
#     # атрибуты класса
#     ushi = 'Есть уши'
#     age = 0

#     def __init__(self, name, age, colour):
#         '''
#         Инициализатор. 
#         Именно здесь определяются аттрибуты обьекта класса
#         '''
#         # В self храниться сам обьект
#         self.name = name # аттрибут экзампляра(обьекта) класса
#         self.colour = colour 
        
# bobik = Dog('Bobik', 'brown')
# yumi = Dog('yumi', 'white')
# print(f'name: {bobik.name}, age: {bobik.age}, colour: {bobik.colour}, {bobik.ushi}')
# print(f'name: {yumi.name}, age: {yumi.age}, colour: {bobik.colour}, {yumi.ushi}')

# bobik.age = 2
# yumi.age = 2

# bobik.ushi = 'Нет ушей'
# yumi.ushi = 'Есть уши'

# print(f'name: {bobik.name}, age: {bobik.age}, {bobik.ushi}')
# print(f'name: {yumi.name}, age: {yumi.age}, {yumi.ushi}')


# import random
# class Human():
#     def __init__(self, name, weight, nationality):
      
#         self.name = name
#         self.age = 0
#         self.weight = weight
#         self.nationality = nationality

#     def birthday(self):
#         print(f'\nHappy Birthday {self.name}')

#         self.age += 1 # self.age = self.age + 1
#         self.weight += random.randint(3, 7)

# human1 = Human('John', 3.700, 'American')
# human2 = Human('Abu-bakr', 3, 'Arab')

# print(human1.name, human1.age, human1.weight, human1.nationality)
# print(human2.name, human2.age, human2.weight, human2.nationality)

# print('After 1 year: ')
# print(human1.birthday())
# print(human2.birthday())

# print(human1.name, human1.age, human1.weight, human1.nationality)
# print(human2.name, human2.age, human2.weight, human2.nationality)

# print('After 3 month: ')
# human1.birthday()

# print(human1.name, human1.age, human1.weight, human1.nationality)
# print(human2.name, human2.age, human2.weight, human2.nationality)


"============================"

class Student():
    univer = 'MIT'
    def __init__(self, name, last_name):
        self.name = name
        self.last = last_name
        self.books = []
        self.languages = {}
        self.knowledge = 0
        self.is_ready_to_work = False

    def add_point(self, point):
        self.knowledge += point
        if self.knowledge >= 500:
            self.is_ready_to_work = True
            print(f'{self.name} is ready to work!!!')

    def read_book(self, book):
        self.books.append(book)
        self.add_point(50)

    def do_lab_works(self):
        self.add_point(50)

    def do_real_project(self):
        self.add_point(100)

    def learn_new_language(self, language, point):
        if not 60 < point <= 100:
            raise Exception('Your point out of range!!')
        self.languages.update({language: point})
        self.add_point(point)

st1 = Student('John', 'Snow')
st2 = Student('Jamie', 'Lanister')

print(st1.name)
print(st2.name)
print('Before study {st1.name}: ', st1.books, st1.knowledge, st1.is_ready_to_work)


st1.read_book('Martin Iden')
st1.read_book('E.Onegin')
st1.read_book('Ants')

st1.do_real_project()
st1.do_lab_works()
st1.do_lab_works()
st1.learn_new_language('Python', 90)
st1.do_real_project()
st1.learn_new_language('JS', 100)

print(st1.name, st1.books, st1.knowledge, st1.languages, st1.is_ready_to_work)
print(st1.univer)

"""
Напишите класс Salary для расчета налогов на заработную плату. 
У класса должна быть обязательная переменная класса - процент налога от зарплаты - 15%. 
Объекты класса должны иметь сумму зарплаты и стаж работы в качестве атрибутов. 
Также у класса должен быть метод расчитывающий сумму налога заплаченного за весь стаж работы. 
Создайте экземпляр класса и посчитайте сумму вашего налога.
"""

# class Salary:
#     tax = 0.15

#     def __init__(self, salary, exp):
#         self.salary = salary
#         self.age_of_work = exp

#     def sum_of_tax(self):
#         result = (self.salary * self.tax) * (self.age_of_work * 12)
#         print(f'Сумма налога составила {result} сомов, за {self.age_of_work} лет работы!')

# john = Salary(150_000, 8)
# john.sum_of_tax()

# class song:
    