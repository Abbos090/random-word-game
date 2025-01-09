"""Funksiyalar"""

def bolinuvchi(n):
    """"""
    lst=[]
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
             lst.append("FizzBuzz")
        elif i%3==0:
             lst.append("Fizz")
        elif i%5==0:
             lst.append("Buzz")
        else:
             lst.append(str(i))
    return lst

   
def umumiy_bolinuvchi(a,b):
     count = 0
     if a>b:
          for i in range(1,b+1):
               if a%i==0 and b%i==0:
                    count+=1
                    print(i,end=" ")
     
     else:
          for i in range(1,a+1):
               if a%i==0 and b%i==0:
                    count+=1
                    print(i,end=" ")
     return count



"""My functions"""
from random import randint as r
def PC_random(a,b):
    number = r(a,b)
    count = 0
    for i in range(10):
        count+=1
        print(f"men {a} dan {b} gacha bitta son o'yladim topingchi >>>")
        m = int(input())

        if m > number:
            print("men o'ylagan son bundan kichikroq")
        elif m < number:
            print("men o'ylagan son bundan kattaroq")
        else :
            print(f"siz {count}ta urinishda topdingiz")
            return count
        if count == 10:
            print("Siz hamma imkoniyatlaringizdan foydalanib bo'ldingiz")
    return count+1

def user_rd(a,b):
    count = 0
    print(f"endi esa siz {a} dan {b} gacha bitta son o'ylang")
    d = input("o'ylagan bo'lsangiz 'enter' tugmasini bosing")
    for i in range(10):
        count += 1
        computer_r = r(a,b)
        print(f"siz {computer_r} son o'yladingiz ('+','-','T' >>>)")
        answer = input()
        if answer == '+':
            a = computer_r + 1
        elif answer == '-':
            b = computer_r - 1
        elif answer.upper() == 'T':
            print(f"men {count}ta urinishda topdim")
            return count
        if count == 10:
            print("kompyuter hamma imkoniyatlaridan foydalanib bo'ldi")
    return count+1

def play(a,b):
    while(True):
        PC = PC_random(a,b)
        UR = user_rd(a,b)
        if PC > UR:
            print(f"Kampyuter {UR}ta urinishda sizni yutdi!!")
        elif PC < UR:
            print(f"Siz {PC}ta urinishda yutdingiz!!")
        else:
            print("Durang")
        again_play = input("Yana o'ynashni hohlaysizmi? (Yes/No)")
        if again_play.lower() == "no":
            break

from math import sqrt

def harf_aniqlash(n):
    if len(n) != 1:
        return 0
    if n.isalpha():
        return 1
    else:
        return 0

def juft_or_toq(n):
    if n%2==0:
        return "even"
    else:
        return "odd"

def maximum(n,m):
    return max(n,m)


from random import randint as r
def game():
    n = int(input("Istalgan son kiriting>>")) 
    count = 0
    for i in range(2):
        m = int(input("taxminingizni kiriting>>".capitalize()))
        if m > n:
            print("Pastga")
        elif m < n:
            print("TEPAGA")
        else:
            print("YORVORDIZ")


from random import choice
def get_word():
    words = [
    "yulduz", "kitob", "uy", "daryo", "tosh"]
    word = choice(words)
    while "'" in word:
        word = choice(words)
    return word.upper()

def display(user_letters,word):
    display_letters = " "
    for letter in word:
        if letter in user_letters.upper():
            display_letters += letter
        else:
            display_letters += "-"
    return display_letters

def play1():
    word = get_word()
    word_letters = set(word)
    user_letters = " "

    s = input("o'yinni boshlashni hohlasangiz 'enter' tugmasini bosing")
    print(f"Men {len(word)} xonali son o'yladim topa olasizmi? >>")
    while len(word_letters) > 0:
        print(display(user_letters,word))
        if len(user_letters) > 1:
            print(f"Siz shu paytgacha {user_letters} harflarni kiritdingiz")
        letter = input("Harf kiriting >>").upper()
        if len(letter) > 1:
            print("1ta harf kiriting iltimos")
            continue
        if letter in user_letters:
            print(f"Siz '{letter}' harfini avval kiritgansiz")
        elif letter in word_letters:
            word_letters.remove(letter)
            print(f"Siz '{letter}' harfini to'g'ri topdingiz")
        else:
            print(f"'{letter}' harfi so'zni ichida yo'q")
        user_letters += letter

    print(f"Tabriklayman siz '{word}' so'zini {len(user_letters)}ta urinishda to'g'ri topdingiz")
    while True:
        answer = input("yana o'ynashni hohlaysizmi? (yes/no)").lower()
        if answer == "yes":
            play1()
        else:
            break



def play2():
    word = get_word()
    word_letters = set(word)
    user_letters = ""

    s = input("o'yinni boshlash uchun 'enter' tugmasini bosing")
    print(f"Men {len(word)} xonali son o'yladim topa olasizmi?")
    
    count1 = 0
    count2 = 0
    while len(word_letters) > 0:
        print(display(user_letters,word))
        if len(user_letters) > 1:
            print(f"Siz shu paytgacha {user_letters} harflarini kiritdingiz")
        answer1 = input("'1-o'yinchi' Bitta harf kiriting>>").upper()
        if len(answer1) > 1:
            print("1ta harf kiriting iltimos")
            continue
        
        if answer1 in user_letters:
            print(f"Siz '{answer1}' harfini avval kiritgansiz")
        elif answer1 in word_letters:
            word_letters.remove(answer1)
            print(f"Siz '{answer1}' harfini to'g'ri topdingiz")
        else:
            print(f"'{answer1}' harfi so'zni ichida yo'q")
        
        user_letters += answer1
        count1+=1

        print(display(user_letters,word))
        answer2 = input("'2-o'yinchi' Bitta harf kiriting>>")
        if len(answer2) > 1:
            print("1ta harf kiriting iltimos")
            continue
        if answer2 in user_letters:
            print(f"Siz '{answer2}' harfini avval kiritgansiz")
        elif answer2 in word_letters:
            word_letters.remove(answer2)
            print(f"Siz '{answer2}' harfini to'g'ri topdingiz")
        else:
            print(f"'{answer2}' harfi so'zni ichida yo'q")
        user_letters += answer2
        count2+=1

    if count1 > count2:
        print(f"2-ishtirokchi {count1 - count2}ta farq bilan yutdi!!")
    elif count1 < count2:
        print(f"1-ishtirokchi {count2 - count1}ta farq bilan yutdi!!")
    else:
        print(f"{count1}ta urinishda durrang!!")

def game1():
    quation = input("1tali o'yinmi yoki 2tali? (1/2)")
    if quation == "1":
        play1()
    elif quation == "2":
        play2()
    else:
        print("Bunday kiritiluvchi yo'q!")


def signup(username, password):
    f = open("users.txt", "a")
    f.write(username, password)
    f.close