"""Homework 17.09.24"""

# print("""Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are""")

# print("""Men kecha Abdulla Avloniyning 
# “Turkiy Guliston yoxud-Tarbiya” 
# asarini o’qidim. """)

# text=str(input())
# print(len(text))

"""Homework 18.09024y"""

# print("We are using \"C18\"")

# print("""######
# #
# #
# #####
# #
# #
# #""")

# print("""    ######
#   ##      ##
#  #
#  #
#  #
#  #
#  #
#   ##      ##
# #     ######""")

# N=int(input())
# M=int(input())
# R=int(input())
# H=int(input())
# print(f"{N}*{M}{R}+{H}={N*M,H+M}")

# a=int(input())
# b=int(input())
# print(f"{a*b}")

# N=int(input())
# print(f"{N*12700}so'm")

"""Homework 19.09.24y"""
# text=input()
# print(text.capitalize())
# print(text.title())
# print(text.upper())
# print(text.count("e"))
# print(text.replace("John","Abbos"))
# print(text.count("the"))
# print(text.replace("the","a"))

"""Homework 20.09.2024"""

# n=input()
# m=input()
# if n>m:
#     print(f"{n}>{m}")
# else:
#     print(f"{n}<{m}")
    
# """2"""
# n=int(input())
# if n%2==0:
#     print("even")
# else:
#     print("odd")
    
# """3"""
# n = int(input())
# m = int(input())
# c = int(input())
# if n<=b<=c:
#     print(f"{n} soni katta {m} va {c} sonlaridan")
# elif m<=n<=c:
#     print(f"{m} soni katta {n} va {c} sonlaridan")
# elif c<=b<=n:
#     print(f"{c} soni katta {n} va {m} sonlaridan")
    
# """4"""
# n = int(input())
# if 20 <= n <=30:
#     print(1)
# else:
#     print(0)


"""Uy ishi 23.09.24y"""



# n=int(input())

# if n>=12 and n<=18:
#     print("o'smir")

# elif n>=19 and n<=30:
#     print("yosh")

# elif n>=31 and n<=45:
#     print("o'rta yosh")
# elif n>45:
#     print("qariya")
# else:
#     print("yosh bola")

# n=int(input())
# m=int(input())

# if m==n*n:
#    print(f"{n}*{n}={m}")
# else:
#    print("None")


"""Uy ishi 23.09.24y"""

# n=int(input())
# m=int(input())

# if n>m:
#     print(f"{n/m}")
# else:
#     print(f"{m/n}
      
# n=int(input())

# if n<0:
#     print("ichkarida o'yna")
# elif 0<=n<=40:
#     print("tashqarida o'yna")
# else:
#     print("ichkarida o'yna")

# n=int(input())

# if n%2==0 and n%3==0 and n%5==0:
#     print("A")
# elif n%3==0 and n%3==0:
#     print("B")
# elif n%2==0 and n%5==0:
#     print("C")
# elif n%3==0 and n%5==0:
#     print("D")
# elif n%2==0 or n%3==0 or n%5==0:
#     print("E")
# else:
#     print("N")

# n=int(input())
# m=int(input())
# s=int(input())

# # if n**2+m**2==s**2:
# #     print("True")
# # elif n**2+s**2==m**2:
# #     print("True")
# # elif m**2+s**2==n**2:
# #     print("True")
# # else:
# #     print("False")

"""uy ishi 24.09.24y"""

# n=int(input())
# if n>=1:
#     print(f"{n+1}")
# else:
#     print(n)

# n=int(input())

# if n>=1:
#     print(f"{n+1}")
# else:
#     print(f"{n-2}")


# n=int(input())

# if n>=1:
#     print(f"{n+1}")
# elif n<0:
#     print(f"{n-2}")
# else:
#     print(f"{n+10}")

# n=int(input())
# m=int(input())
# s=int(input())

# if n>0 and m>0 and s>0:
#     print("3")
# elif n>0 and m<0 and s>0:
#     print("2")
# elif n>0 and m>0 and s<0:
#     print("2")
# elif n<0 and m>0 and s>0:
#     print("2")
# elif n>0 and m<0 and s<0:
#     print("1")
# elif n<0 and m<0 and s>0:
#     print("1")
# elif n>0 and m>0 and s<0:
#     print("1")
# else:
#     print("0")


# n=int(input())
# m=int(input())

# if n>m:
#     print("n")
# else:
#     print("m")

# n=int(input())
# m=int(input())

# if n<m:
#     print("n")
# else:
#     print("m")

# n=int(input())
# m=int(input())

# if n>m:
#     print(f"{n,m}")
# else:
#     print(f"{m,n}")

"""Homework 26.09.24"""

"""1"""
# i=2
# while i<=10:
#     if i%2==0:
#         print(i)
#     i+=1

"""2"""
# sum=0
# i=1

# while i<=10:
#     sum+=i
#     i+=1
# print(sum)

"""3"""
# n=int(input())
# sum=0
# i=1

# while i<=n:
#     sum+=i
#     i+=1
# print(sum)

"""4"""
# a=int(input())
# b=int(input())
# i=1
# sum=0

# while i<=b or i<=a:
#     if i%2==0:
#         sum+=i
#         i+=1
#     print(sum)

"""5"""
# a=int(input())
# b=int(input())
# print(f"{a**b}")

"""6"""
# n=int(input("son kiriting"))
# i=1
# while i<=10:
#     print(f"{n}*{i}={n*i}")
#     i+=1

"""7"""
# n=int(input())
# i=1
# sum=n

# while i<=n:
#     i+=1
#     sum*=1
# print(sum)

"""8"""
# while True:
#     son=(input())
#     if son=="0":
#         print("tizim to'xtatildi")
#         break

"""Homework 27.09.24y"""
"""1"""
# N=int(input())
# i=0
# for i in range(1,N+1):
#     if i%2==0:
#       print(i,end=" ")

"""2"""
# N=int(input())
# i=0
# for i in range(1,N+1):
#     if i%2!=0:
#       print(i,end=" ")

"""3"""
# N=int(input())
# i=1
# for i in range(N,0,-1):
#     print(i,end=" ")

"""4"""
# N=(input())
# i=0
# for i in range(len(N)):
#     if N[i].isalpha():
#      i+=1

# print("textda shuncha : ",i," ta harf bor")

"""5"""
# N=int(input())
# i=1
# sum=0
# for i in range(1,N+1):
#     sum=sum+i 
# print(sum)   
        
"""6"""
# N=int(input())
# i=1
# for i in range(1,N+1):
#     if i%3==0:
#         print(i,end=" ")
"""7"""
# N=(input)()

# for i in range(len(N)-1, -1, -1):
  
#  print(N[i],end="")

"""Takrorlash"""
# a=5
# b=6
# a-=2
# b*=1
# print({a-b})

# print("Men bugun ishladim va\ndam oldim")

# text="life is good" 
# print(text[:4])
# print(text[::-1])
# print(text[1:7])

# print(text.capitalize())
# print(text.lower())
# print(text.title())
# print(text.upper())
# print(text.index("o"))
# print(text.count("q"))
# print(text.isalpha())
# print(text.isalnum())
# print(text.isdigit())
# print(text.isupper())
# print(text.islower())
# print(text.replace("is","or"))
# print(text.casefold())
# print(text.center("good","is"))
# print(3>4 and 3<5)
# text="Abbosakoo"
# print(text[2:5])



"""04.10.24y"""

"""1"""

# n=int(input())
# sum=0
# for i in range(1,n//2+1):
#     if n%i==0:
#         sum+=i

# if sum==n:print("perfect son")
# else:print("perfect emas")

"""2"""

# n=int(input())
# sum=0
# while n>=0:
#         sum+=(n%10)**3
#         n//10
# print(sum)

"""3"""

# n=(input())
# text = n[::-1]
# print(text)

"""4"""

# n=int(input())
# sum=0
# for i in range(1,n//2+1):
#     if n%i==0:
#         sum+=i

# print(sum)
"""uy ishi 07.10.24y"""

"""1"""

# mevalar=["anor","olma","olxo'ri","nok","o'rik","ananas","olcha","gilos","bexi","mandarin"]
# print(mevalar[::-1])

"""2"""

# ismlar=["Mark","Eon","Rokfeller","Jeff","Bill"]
# ismlar[-1]="Abbos"
# print(ismlar)


"""3"""

# sonlar=["1","2","3","4","5"]
# raqamlar=["6","7","8","9"]
# sanoqsonlar=sonlar+raqamlar
# print(len(sanoqsonlar))

"""4"""

# sonlar=[5,10,15,20,25]
# n=int(input())
# if n in sonlar:print("True")
# else:print("False")


"""07.10.24y"""


"""1"""

# n=int(input())
# numbers=[]
# for i in range(n):
#     num=int(input())
#     numbers.append(num)
# max=max(numbers)
# print(max)

"""2"""

# n=int(input())
# numbers=[]
# for i in range(n):
#     num=int(input())
#     numbers.append(num)
# min=min(numbers)
# print(min)

"""4"""

# n=int(input())
# numbers=[]
# for i in range(n):
#     num=int(input())
#     numbers.append(num)
# sum=sum(numbers)
# print(sum)

"""5"""

# n=int(input())
# numbers=[]
# for i in range(n):
#     num=int(input())
#     numbers.append(num)
# sum=sum(sum) 


"""10.10.24y"""


"""1"""
# tpl=(4, 7, 9, 2, 6)
# print(tpl[1::2])

"""2"""
# tpl1=(1,2,3,)
# tpl2=(4,5,6,)
# tpl3=tpl1+tpl2
# print(tpl3)

"""3"""
# tpl=(10, 20, 30, 40, 50, 60)
# print(tpl[2:5])

"""4"""
# tpl=(1,2,3,4,5)
# print(len(tpl))

"""5"""
# tpl=(1,2,3,4,5)
# print(3 in tpl)

"""6"""
# tpl=(1,2,3,4,5)
# tpl=list[tpl]
# print(tpl)

"""7"""
# tpl=(10,27,92,18)
# print(max(tpl))
# print(min(tpl))

"""8"""
# tpl=(18,91,38,36,39,84,47)
# print(tpl.count(38))

"""9"""
# tpl=(83,37,276,83,376,398,91)
# tpl2=tuple(sorted(tpl))
# print(tpl2)

"""uy ishi 11.10.24y"""

"""1"""
# my_sets={1,2,3,4,5}
# for i in (my_sets):
#     print(i,end=" ")

"""2"""
# my_sets={1,2,3,4,5}
# my_sets.add(6)
# print(my_sets)

"""3"""
# my_sets={1,2,3,4,5}
# my_sets.remove(5)
# print(my_sets)

"""4"""
# my_sets={1,2,3,4,5,6,0,7,4,5,7}
# print(len(my_sets))

"""5"""
# my_set={1,2,3}
# my_set2={4,5,6}
# set1=my_set.union(my_set2)
# print(set1)


"""uy ishi 14.10.24y"""
"""1"""
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# set = A.intersection(B)
# print(set)

"""2"""
# A = {1, 2, 3, 4}
# A.discard(5)
# print(A)

"""3"""
# A = {1, 2}
# B = {2, 3}
# C = {3, 4}
# n = A.union(B,C)
# print(n)

"""4"""
# A = {1, 2, 3, 4}
# B = {3, 4, 5}
# set = A.difference(B)
# print(set)

"""5"""
# A = {1, 2, 3}
# B = {2, 3, 4}
# set = A.symmetric_difference(B)
# print(set)

"""6"""
# A = {1, 2, 3}
# A.add(4)
# print(A)

"""7"""
# A = {1, 2}
# B = {1, 2, 3}
# set = A.issubset(B)
# print(set)


"""uy ishi 16.10.24y"""


# text="this is a test this is only a test"
# lst=text.split(" ")
# dct={}
# for i in lst:
#     dct[i]=lst.count(i)
# print(dct)


# dct={}
# n=int(input("Count Student"))
# for i in range(n+1):
#     Name=input("students's name")


"""18.10.24y"""

#          "int":"sonlar",
#          "float":"Kasir sonlar",
#          "list":"R'yxat",
#          "str":"Butun son",
#          "ism":"Sharifjon",
#          "familiya":"Shukurjonov",
#          "yosh":16,
#          "Tug'ulgan yil":2008}
# n=input()
# if n in my_dict:
#     print(f"{n} - {my_dict[n]}")
# else:
#     print("Bunday so'z lug'atimizda yo'q")

"""17.10.24y"""
"""1"""
# n=input()
# dct={}
# lst=n.split(" ")
# for i in lst:
#     dct[i]=lst.count(i)
# print(dct)

"""2"""
# n=int(input())
# dct={}
# for i in range(n):
#     ism=input("O'quvchining ismini kiriting >> ")
#     baxo=int(input("Nechta fandan baxo qo'ymoqchisiz >> "))
#     my_dict[ism]=[int(input("Baxo kiriting >> ")) for j in range(baxo)]
#     my_dict[ism]=sum(my_dict[ism])/baxo
# print(f"{my_dict}")

"""3"""
# grades = {'Ali': [90, 85, 92], 'Laylo': [78, 85, 88], 'Hasan': [92, 91, 89]}
# average_grades = {}
# for student, scores in grades.items():
#     average = sum(scores) / len(scores)
#     average_grades[student] = average
# print(average_grades)

"""4"""
# text = "apple banana apple orange banana apple"
# words = text.split()
# one = set(words)
# print(one)

"""5"""
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# common_elements = set1.intersection(set2)
# print(common_elements)


"""20.10.24y"""

"""1"""
# n=int(input())
# if n<0:print("son manfiy")
# elif n==0:print("nol")
# else:print("son musbat")

"""2"""

# def kvadrat(a):
#     return a**2
# def kub(a):
#     return a**3
# n=int(input())
# sum=kvadrat(n)
# print(sum)
# sum=kub(n)
# print(sum)

"""10"""
# def unlilar(satr):
#     unli_harflar = 'aeiouAEIOU'  
#     hisob = 0
    
#     for harf in satr:
#         if harf in unli_harflar:
#             hisob += 1
#     return hisob
# satr = "hello"
# print( {unlilar(satr)})
   
"""22.10.24y"""
"""1"""

# def sum_and_ortacha(numbers):
#     sum = sum(numbers)
#     average = sum / len(numbers)
#     return (sum, average)
# numbers = [2, 4, 6, 8]
# hammasi = sum_and_ortacha(numbers)
# print(hammasi)

# """2"""
# def reverse_string(s):
#     return s[::-1]
# s = "hello"
# hammasi = reverse_string(s)
# print(hammasi)

# """3"""
# def kopaytma_number(n):
#     return n * 2
# n = 5
# hammasi = kopaytma_number(n)
# print(hammasi)
###1
# numbers = [2, 4, 6, 8]
# def sum_and_qiymat(numbers):
#     total_sum = sum(numbers)
#     average = total_sum / len(numbers)
#     return (total_sum, average)
# result = sum_and_qiymat(numbers)
# print(result)

###2
# s = "hello"
# def reverse_string(s):
#     return s[::-1]
# result = reverse_string(s)
# print(result)

###3
# def kopaytma_number(n):
#     return n * 2
# n = int(input())
# result = kopaytma_number(n)
# print(result)

###4

# numbers = [-5, 3, 0, 9, -1]
# def musbat_sonlar(numbers):
#     for i in numbers:
#         if i>0:
#             return i
#     print(i)  

"""23.10.24y"""

"""1"""
# qoshiluvchi=(lambda a,b:a+b) (int(input()), int(input()))
# print(qoshiluvchi)

"""2"""

# kvadrat=(lambda a:a**2) (int(input()))
# print(kvadrat)

"""3"""

# len=(lambda matn:len(matn)) (input())
# print(len)

"""4"""

# aniqlash=lambda a:"Positive"if a>0 else "Negative" if a<0 else "Zero" 
# son=(float(input()))
# natija=aniqlash(son)
# print(natija)

"""5"""

# a=[3, 5, 7, 2, 8, 10]

# katta_son=(lambda a:a.max())
# print(katta_son)

"""23.10.2024y"""
"""1"""
# kopaytma=lambda a: a**2
# lst=[1, 2, 3, 4, 5]
# print(list(map(kopaytma,lst)))

"""2"""
# len_1 = lambda text: len(text)
# text = input("Matn kiriting >> ")
# uzunlik = len_1(text)
# print(uzunlik)

"""3"""
# kopaytma=lambda a: a*3
# lst=[1, 2, 3, 4, 5]
# print(list(map(kopaytma,lst)))


"""5"""
# text=["a","b","c","d"]
# def katta(text):
#     return text.upper()
# print(list(map(katta,text)))

"""25.10.24y"""




###2
# def juft_sonlar(t):
#     return t[::2]
# input_tuple = (10, 15, 20, 25, 30, 35)
# output = juft_sonlar(input_tuple)
# print(output)

###3
# def qiymatga_kora_tartiblash(lugat):
#     return dict(sorted(lugat.items(), key=lambda item:item[1] ))

# lugat1 = {'ali': 85, 'vali': 90, 'hasan': 78, 'hoshim': 92}
# output = qiymatga_kora_tartiblash(lugat1)
# print(output)

###4
# def kesishma(set1, set2):
#     return set1.intersection(set2)
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# result = kesishma(set1, set2)
# print(result)

###5
# def uzunligi(nested_list):
#     return [len(inner_list) for inner_list in nested_list]
# input_list = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
# result = uzunligi(input_list)
# print(result)

###6
# def almashtirish(tup):
#     if len(tup) < 2:
#         return tup 
#     new_tup = tup[:1] ,[-1]
#     return new_tup
# input_tuple = (1, 2, 3, 4, 5)
# result = almashtirish(input_tuple)
# print(result)


"""28.10.24y"""

# ###2
# numbers = (10, 15, 20, 25, 30, 35)
# for i in numbers:
#     if i%2==0:
#         print(f"juft son- {i}")

# ###3
# lugat = {'vali': 90, 'hasan': 78, 'hoshim': 92,'ali': 85}
# sorted(lugat)
# print(lugat)

# ###4
# my_sets = {1, 2, 3, 4, 5}
# my_sets2 = {3, 4, 5, 6, 7}

# def diference(my_sets,my_sets2):
#     return my_sets.intersection(my_sets2)
# result = diference(my_sets,my_sets2)
# print(result)

# ###5
# my_list = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]

# def lst_len(my_list):
#     return len(my_list)
# print(lst_len(my_list))

###6


# def change(tpl):
#     tpl=list(tpl)
#     tpl[1],tpl[-1] = tpl[-1],tpl[1]
#     return tpl
# tpl=(1, 2, 3, 4, 5)
# print(change(tpl))

###7

# dct = {'ali': 85, 'vali': 90, 'hasan': 78, 'hoshim': 92}
# def max_min(dct):
#     maximum = max(dct.values())
#     minimum = min(dct.values())
#     return(maximum,minimum)
# print(max_min(dct))

###8

# sets = {5, 10, 15, 20, 25}
# def big_diference(sets):

"""29.10.24y"""

# ###1
# def summa(*args):
#     return sum(args)
# print(summa(1,2,3,4,5))
# print(summa(10,20,30,40,50))

# ###2
# def person_info(**info):
#     pass
# dct={"ism":"Abbos","yosh":12,"FAmiliya":"Zafarxo'jayev"}
# print(person_info(dct))

# ###3
# def full_info(*args):
#     return sum(args)
# print(full_info(10,20,30))


"""15.11.24y"""
#1
# text = "hello world"
# print(len(text))

#2
# text = "hello world"
# print(text.capitalize())

#3
# text = "     assalomu      alaykum      azizlar"
# text = text.split()
# for i in text:
#     print(i,end=" ")

#4
# text = "dorixona".capitalize()

# print(text.replace("x"," "))

"""18.11.24"""

# #1
# a,b,c = int(map(input())).sprit()
# print(a,b,c)


