from random import randint as r

def sontop(x):
    son = r(1,100)
    start = input("O'yinni boshlash uchun 'enter' tugmasini bosing")
    ism = input("Ismingizni kiriting >> ")
    print(f"{ism.capitalize()} men 1dan 100gacha bitta son o'yladim topa olasizmi ? ")
    ans = int(input("Ixtiyoriy son kiriting >> "))
    while True:
        if ans > son:
            print(f"{ans}dan kichikroq son kiriting")
        elif ans < son:
            
