# Принципы в ООП: 
# 1. Наследования
# 2. Инкапсуляция
# 3. Полиморфизм

# 4. Абстракция
# 5. Композиция
# 6. Агрегация

# Наследования позволяет принимать родительские методы, атрибуты и поведение

# Родительский класс
# Дочернbй класс

#------------------------------------

# class Animal:
#     def say(self):
#         print('I\'m Aminal!')

# class Croco(Animal):
#     pass

# croco = Croco()
# croco.say()

# -----------------------------------

# class Employee:
#     bonus = 1.5
#     def __init__(self, name, last_name, salary):
#         self.name = name
#         self.last_name = last_name
#         self.salary = salary

#     def get_full_name(self):
#         return f'{self.name} {self.last_name}'

#     def give_bonus(self):
#         self.salary = self.salary * self.bonus

# em1 = Employee('John', 'Snow', 800)
# print(em1.get_full_name())
# print(em1.salary)
# em1.give_bonus()
# print(em1.salary)

# ----------------------------------

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def info(self):
#         print(f'My name is {self.name} and I am {self.age}')
    
# class Student(Person):
#     def __init__(self, name, age, univer):
#         super().__init__(name, age)
#         self.univer = univer
    
#     def info(self):
#         super().info()
#         print(f'I study in univer {self.univer}')

# mike = Student('Manas', 17, 'KSLA')
# mike.info()

# ----------------------------------

# class Employee:
#     bonus = 1.5
#     def __init__(self, name, last_name, salary):
#         self.name = name
#         self.last_name = last_name
#         self.salary = salary

#     def get_full_name(self):
#         return f'{self.name} {self.last_name}'

#     def give_bonus(self):
#         self.salary = self.salary * self.bonus

# class Developer(Employee):
#     def __init__(self, name, last_name, salary, prog_lang):
#         super().__init__(name, last_name, salary)
#         self.progl_ang = prog_lang


# class Manager(Employee):
#     def __init__(self, name, last_name, salary, emps=None):
#         super().__init__(name, last_name, salary)
#         if emps == None:
#             self.emps = []
#         else:
#             self.emps = emps
    
#     def add_emps(self, emp):
#         if emp not in self.emps:
#             self.emps.append(emp)
#         else:
#             print('Employee already is in!!!')
    
#     def show_emps(self):
#         result = []
#         for emp in self.emps:
#             result.append(emp.get_full_name())
#         return result

# dev1 = Developer('John', 'Snow', 1500, 'JS')
# dev2 = Developer('Manas', 'Kaiymov', 2000, 'Python')
# dev3 = Developer('Dastan', 'Samatov', 2300, 'Python')
# dev4 = Developer('Beka', 'Sultanov', 1000, 'JS')

# manager1 = Manager('Ivan', 'Ivanov', 3000, emps=[dev2, dev3])
# manager2 = Manager('Aibek', 'Velikiy', 1500)

# manager2.add_emps(dev1)
# manager2.add_emps(dev4)

# print(manager1.show_emps())
# print(manager2.show_emps())


# print(f'Manager {manager1.get_full_name()}, has {manager1.show_emps()} developers. His salary is ${manager1.salary}')
# print(f'Manager {manager2.get_full_name()}, has {manager2.show_emps()} developers. His salary is ${manager2.salary}')

# --------------------------------------------------

# from email.mime import image
# from turtle import title


# class Post:
#     def __init__(self, user):
#         self.user = user
#         self.posts = []
#         self.id = 0

#     #CRUD

#     def creat_post(self, title, body, image):
#         self.id += 1
#         post = dict(id=self.id, title=title, body=body, image=image)
#         self.posts.append(post)
#         return {'status': 201, 'msg': 'Successfully created'}
    
#     def retrieve_post(self, post_id):
#         for post in self.posts:
#             if post.get('id') == post_id:
#                 return post
#             return {'status': 404, 'msg': 'not found!'}
#     def update_post(self, post_id, **kwargs):
#         for post in self.posts:
#             if post.get('id') == post_id:
#                 post.update(kwargs)
#                 return {'status': 200, 'msg': 'Updated'}
#         return {'status': 404, 'msg': 'not found!'}

#     def delete_post(self, post_id):
#         for post in self.posts:
#             if post.get('id') == post_id:
#                 index_post = self.posts.index(post)
#                 self.post.pop(index_post)
#                 return {'status': 204, 'msg': 'No contend, deleted'}
#         return {'status': 404, 'msg': 'not found!'}


# acc1 = Post('John Snow')
# acc2 = Post('Mike Tison')

# acc1.creat_post('Good news', 'Моя сестра родила дочку', 'https://photo.jpg')
# acc1.creat_post(
#     'На прогулке я спас собаку от голода', 'Вот фото', 'https://dasas.jpg'
# )
# acc1.creat_post('ИУУУУУУ', 'Мама я в Дубае', 'https://wew.jpg')

# print(acc1.update_post(2, title = 'Progulka updated', body = 'Its cool', image='https://2323dfd.jpg'))

# print(acc1.retrieve_post(2))
# print(acc1.posts)