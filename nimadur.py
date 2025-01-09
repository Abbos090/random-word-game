"""1"""
# import turtle as r
# import colorsys as sm
# r.tracer(2)
# r.bgcolor("black")
# r.pensize(2)
# n=100
# h=0
# for i in range(500):
#     for i in range(4):
#         c=sm.hsv_to_rgb(h,1,1)
#         h+=1/n
#         r.color(c)
#         r.circle(49+i*5,90)
#         r.forward(100)
#         r.left(90)
#     r.right(10)
# r.done()

"""2"""
# from turtle import*
# import colorsys
# speed(0)
# pensize(2)
# bgcolor("black")
# h=0.8

# for i in range(100):
#     c=colorsys.hsv_to_rgb(h,1,1)
#     color(c)
#     h+=0.004
#     for j in range(4):
#         fd(i)
#         rt(20)
#     rt(120)
# done()

"""3"""
# """hamma sonni kvadrati"""

# def kvadratlarni_chiqar(eng_kichik, eng_katta):
#     for i in range(eng_kichik, eng_katta + 1):
#         kvadrat = i ** 2
#         print(f"{i} ning kvadrati: {kvadrat}")

# kvadratlarni_chiqar(1,100)

# n=int(input())
# def kvadrat(n):
#     return n**2
# result=kvadrat(n)
# print(result)

"""4"""

# #kalendar
# import calendar
# yy=int(input("qaysi yilni topishimni hohlaysiz >>>"))
# mm=int(input("qaysi oyni topishni hohlaysiz >>>"))
# print(calendar.month(yy,mm))

# class Talaba:
#     def __init__(self, ism, familiya, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil

# talaba1 = Talaba('Abbos', 'Zafarxo\'jayev', 2009)

# print(talaba1.ism)


"""Yurak"""

# from turtle import *
# from math import sin, cos
# bgcolor("black")
# speed(100)
# color("red")
# pensize(2)
# def heart(n):
#     x = 15 * sin(n)**3
#     y = 12 * cos(n) - 5*\
#         cos(2*n) - 2*\
#         cos(3*n) - \
#         cos(4*n) 
    
#     return x,y

# for i in range(18):
#     pendown()
#     for j in range(100):
#         x , y = heart(j/15)
#         goto(x*i, y*i)
#     penup()
#     hideturtle()
# done()
