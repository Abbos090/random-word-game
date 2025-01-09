
from random import choice
def get_word():
    words = ['kitob', 'qalam', 'stol', 'oila', 'bola', 'ota', 'ona', 'bahor', 'yoz', 'kuz',
 'qish', 'uy', 'maktab', "do'st", 'daryo', "tog'", "bog'", 'shahar', 'qishloq', 'oy',
 'kun', 'hafta', 'yil', "yo'l", 'qush', 'it', 'mushuk', 'suv', 'havo', 'osmon',
 'quyosh', 'oy', 'yulduz', 'daraxt', 'gul', 'kitobxona', 'talaba', "o'quvchi", 'ustoz', 'dars',
 'ish', 'qishloq', 'tandir', 'non', 'sut', 'shakar', 'qand', 'tuz', "go'sht", 'ovqat',
 'meva', 'sabzavot', 'olma', 'nok', 'uzum', 'shaftoli', 'gilos', 'anor', 'banan', 'apelsin',
 'limon', 'sabzi', 'kartoshka', 'piyoz', 'pomidor', 'bodring', 'qovoq', 'salat', "sho'rva", 'osh',
 'choy', 'qahva', "ko'rpa", "ko'ylak", 'shim', 'oyoq', 'oyoq kiyim', "qo'lqop", 'shapka', 'paypoq',
 'sumka', 'soat', 'telefon', 'kompyuter', 'internet', 'gazeta', 'radio', 'televideniye', 'kino', 'muzey',
 'teatr', 'konsert', 'sport', 'futbol', 'tennis', 'basketbol', 'volleybol', 'yugurish', 'suzish', 'velosiped']

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
            display_letters += " - "
    return display_letters

def play1():
    word = get_word()
    word_letters = set(word)
    user_letters = " "

    s = input("o'yinni boshlashni hohlasangiz 'enter' tugmasini bosing")
    print(f"Men {len(word)} xonali so'z o'yladim topa olasizmi? >>")
    while len(word_letters) > 0:
        print(display(user_letters,word))
        if len(user_letters) > 1:
            print(f"Siz shu paytgacha '{user_letters}' harflarni kiritdingiz")
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
            game1()
        else:
            break



def play2():
    word = get_word()  # Tasodifiy so'z generatsiya qiluvchi funksiya
    word_letters = set(word)
    user_letters = ""

    input("O'yinni boshlash uchun 'Enter' tugmasini bosing.")
    print(f"Men {len(word)} xonali so'z o'yladim. Topa olasizmi?")


    while len(word_letters) > 0:
        print(display(user_letters, word))
        if len(user_letters) > 1:
            print(f"Siz shu paytgacha '{user_letters}' harflarini kiritdingiz.")

        # 1-o'yinchining navbati
        answer1 = input("'1-o'yinchi' bitta harf kiriting >> ").upper()
        if len(answer1) > 1:
            print("Iltimos, faqat 1ta harf kiriting.")
            continue
        if answer1 in user_letters:
            print(f"Siz '{answer1}' harfini avval kiritgansiz.")
        elif answer1 in word_letters:
            word_letters.remove(answer1)
            print(f"Siz '{answer1}' harfini to'g'ri topdingiz.")
            if len(word_letters) == 0:  # So'nggi harfni topish holati
                print(f"1-o'yinchi {word} so'zini topdi va g'olib bo'ldi!")
                return
        else:
            print(f"'{answer1}' harfi so'z ichida yo'q.")

        user_letters += answer1

        # 2-o'yinchining navbati
        print(display(user_letters, word))
        answer2 = input("'2-o'yinchi' bitta harf kiriting >> ").upper()
        if len(answer2) > 1:
            print("Iltimos, faqat 1ta harf kiriting.")
            continue
        if answer2 in user_letters:
            print(f"Siz '{answer2}' harfini avval kiritgansiz.")
        elif answer2 in word_letters:
            word_letters.remove(answer2)
            print(f"Siz '{answer2}' harfini to'g'ri topdingiz.")
            if len(word_letters) == 0:  # So'nggi harfni topish holati
                print(f"2-o'yinchi {word} s'zini topdi va g'olib bo'ldi!")
                return
        else:
            print(f"'{answer2}' harfi so'z ichida yo'q.")

        user_letters += answer2

    print("O'yin tugadi.")



def game1():
    quation = input("1 kishilik o'ynashni tanlaysizmi yoki 2 kishilikmi (1/2) >> ")
    if quation == "1":
        play1()
    elif quation == "2":
        play2()
    else:
        print("Bunday kiritiluvchi yo'q!")


game1()