
"""class"""

# class MyClass:
#     x = 5

# print(MyClass.x)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# pi = Person("Abbos", 16)

# print(pi.name)
# print(pi.age)

# print(pi)

# class Person:
#     def __init__(self, name, age):
#         self.ism = name
#         self.yosh = age
        
#     def __str__(self):
#         return f"{self.ism}({self.yosh})"

# pi = Person("Abbos", 16)
# print(pi)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def myfunc(self):
#         print("Hello my name is " + self.name)
    
# pi = Person("Abbos", 16)
# pi.myfunc()

# class Person:
#     def __init__(my, name, age):
#         my.name = name
#         my.age = age
    
#     def myfunc(a):
#         print(f"Hello my name is {a.name} and my age is {a.age}")

# pi = Person("Abbos",16)
# pi.age = 15
# pi.name = "Sardor"
# del pi
# pi.myfunc()

# class Person:
#     pass


# class Person:
#     def __init__(self, fname, lname):
#         self.lastname = lname
#         self.firstname = fname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     pass

# x = Student("Mike", "Tayson")
# x.printname()

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
    
#     def printname(self):
#         print(self.firstname, self.lastname, self.graduetionyear)        
    
# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)
#         self.graduetionyear = 2019

# x = Student("Mike","Tayson")
# x.printname()
# print(x.graduetionyear)

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.grad = year

#     def welcome(self):
#         print("Welcome", self.firstname, self.lastname, "to the my class of", self.grad)

# x = Student("Mike", "Tayson", 2025)        
# x.welcome()

# class Person:
#     def __init__(self, name, surename, passport, b_year):
#         self.name = name
#         self.surename = surename
#         self.passport = passport
#         self.b_year = b_year

#     def get_info(self):
#         info = f"{self.name} {self.surename}"
#         info += f" passport raqami:{self.passport} {self.b_year}-yilda tug'ilgan"
#         return info
#     def get_age(self):
#         return 2025 - self.b_year

# class Student(Person):
#     def __init__(self, name, surename, passport, b_year, ID_number, adress):
#         super().__init__(name, surename, passport, b_year)
#         self.stage = 1
#         self.ID_number = ID_number
#         self.adress = adress

#     def get_info(self):
#         info = f"{self.name} {self.surename},"
#         info += f" passport raqami:{self.passport}, {self.b_year}-yilda tug'ilgan,"
#         info += f" IDraqami:{self.ID_number}"
#         return info
    
#     def get_stage(self):
#         return self.stage

# class Adress:
#     def __init__(self, house, street, district, region):
#         self.house = house
#         self.street = street
#         self.district = district
#         self.region = region

#     def get_adress(self):
#         info = f"{self.region} viloyati, {self.district} tumani, {self.street} ko'chasi {self.house}-uy"
#         return info

    
# talaba1_manzil = Adress(32,"Bodomzor","Zangiota","Toshkent")
# talaba1 = Student("Abbos","Zafarxo'jayev","FF7763321",2009,"ED322383",talaba1_manzil)

# # print(talaba1.adress.get_adress())


# mytuple = ("banana", "aplle","apricot")
# myit = iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))

# class MyNumber:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x

# myClass = MyNumber()
# myit = iter(myClass)

# print(next(myit))

# class MyNumber:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else: raise StopIteration

# myclass = MyNumber()
# myiter = iter(myclass)
# for i in myiter:
#     print(i)

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     if self.a <= 20:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration

# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myiter:
#   print(x)

"""07.01.25"""
# from uuid import uuid4
# class Avto:
#     def __init__(self, make, model, price, color, km=0):
#         self.make = make
#         self.model = model
#         self.price = price
#         self.color = color
#         self.__km = km
#         self.__id = uuid4()

#     def get_km(self):
#         return self.__km
#     def get_id(self):
#         return self.__id
#     def add_km(self, km):
#         if km >= 0:
#             self.__km += km
#         else:
#             print("Mashinaning kilometrini kamaytirib bo'lmaydi !")

# avto1 = Avto("GM", "Gentra", 30000, "Black", 0 )
# print(avto1.price)

# avto1.add_km(200)
# print(avto1.get_km())

"""08.01.25y"""

# class Car:
#     def __init__(self, brand, model ):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("Zo'r!")

# class Boat:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("O'rtacha!")
# class Plane:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("Oddiy!")

# car1 = Car("Ford", "Mustang")
# boat1 = Boat("Ibiza", "Touring 20")
# moto1 = Plane("Boing", "747")

# for i in (car1, boat1, moto1):
#     i.move()
#     print(i.brand)
#     print(i.model)
