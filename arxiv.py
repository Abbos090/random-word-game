
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
    ishtirokchi = input("Xurmatli ishtirokchi o'z ismingizni kiriting >> ")
    print(f"Men {len(word)} xonali so'z o'yladim topa olasizmi? >>")
    while len(word_letters) > 0:
        print(display(user_letters,word))
        if len(user_letters) > 1:
            print(f"{ishtirokchi.capitalize()} siz shu paytgacha {user_letters} harflarni kiritdingiz")
        letter = input(f"{ishtirokchi.capitalize()} harf kiriting >>").upper()
        if len(letter) > 1 and len(letter) != len(word):
            print(f"{ishtirokchi.capitalize()} 1ta harf kiriting iltimos")
            continue
        if letter in user_letters:
            print(f"{ishtirokchi.capitalize} siz '{letter}' harfini avval kiritgansiz")
        elif letter in word_letters:
            word_letters.remove(letter)
            print(f"{ishtirokchi.capitalize()} siz '{letter}' harfini to'g'ri topdingiz")
        elif letter not in word_letters and len(letter) != len(word):
            print(f"'{letter}' harfi so'zni ichida yo'q")
        
        if len(letter) == len(word) and letter == word:
            print(f"Tabriklayman {ishtirokchi} siz {word} so'zini to'g'ri topdingiz")
            break
        elif len(letter) == len(word) and letter != word:
            print("Afsuski siz xato javob kiritdingiz yana urinib ko'ring")
        user_letters += letter

    print(f"Tabriklayman siz '{word}' so'zini {len(user_letters)}ta urinishda to'g'ri topdingiz")
    while True:
        answer = input("yana o'ynashni hohlaysizmi? (yes/no)").lower()
        if answer == "yes":
            game1()
        else:
            break



def play2():
    word = get_word()
    word_letters = set(word)
    user_letters = ""

    s = input("o'yinni boshlash uchun 'enter' tugmasini bosing")
    ishtirokchi1 = input("1-ishtirokchi o'z ismingizni kiriting >> ")
    ishtirokchi2 = input("2-ishtirokchi o'z ismingizni kiriting >> ")
    print(f"Men {len(word)} xonali so'z o'yladim topa olasizmi?")
    while len(word_letters) > 0:
        print(display(user_letters,word))
        if len(user_letters) > 1:
            print(f"Siz shu paytgacha {user_letters} harflarini kiritdingiz")
        answer1 = input(f"{ishtirokchi1.capitalize()} bitta harf kiriting >> ")
        answer1 = answer1.upper()
        count1 = 0
        javob1 = 0
        if len(answer1) > 1 and answer1 != word and len(answer1) < len(word):
            print("1ta harf kiriting iltimos")
            continue
        elif len(answer1) == len(word) and answer1.upper() != word:
            print("Siz xato javob berdingiz!")
        
        if answer1 in user_letters:
            print(f"Siz '{answer1}' harfini avval kiritgansiz")
        elif answer1 in word_letters:
            word_letters.remove(answer1)
            print(f"Siz '{answer1}' harfini to'g'ri topdingiz")
            count1 += 1
            if len(word_letters) == 0:
                break
        elif answer1 not in word_letters and len(answer1) != len(word):
            print(f"'{answer1}' harfi so'zni ichida yo'q")
        
        if answer1.upper() == word:
            javob1 += 1
            break
        
        user_letters += answer1
        

        print(display(user_letters,word))
        answer2 = input(f"{ishtirokchi2.capitalize()} bitta harf kiriting >> ")
        answer2 = answer2.upper()
        count2 = 0
        javob2 = 0
        if len(answer2) > 1 and answer2 != word and len(answer2) < len(word):
            print("1ta harf kiriting iltimos")
            continue
        elif len(answer2) == len(word) and answer2.upper() != word:
            print("Siz xato javob berdingiz!")

        if answer2 in user_letters:
            print(f"Siz '{answer2}' harfini avval kiritgansiz")
        elif answer2 in word_letters:
            word_letters.remove(answer2)
            print(f"Siz '{answer2}' harfini to'g'ri topdingiz")
            count2 += 1
        elif answer2 not in word_letters and len(answer2) != len(word):
            print(f"'{answer2}' harfi so'zni ichida yo'q")
        
        if answer2.upper() == word:
            javob2 += 1
            break

        user_letters += answer2
        
    if javob1 == 1:
        print(f"{ishtirokchi1.capitalize()} {word} so'zini to'g'ri topib o'yinimiz g'olibi bo'ldi! 🥳")
    elif javob2 == 1:
        print(f"{ishtirokchi2.capitalize()} {word} so'zini to'g'ri topib o'yinimiz g'olibi bo'ldi! 🥳")
    elif count1 > count2:
        print(f"{ishtirokchi1.capitalize()} {count1}ta harf topib, o'yinimiz g'olibi bo'ldi! 🥳")
    elif count2 > count1:
        print(f"{ishtirokchi2.capitalize()} {count2}ta harf topib, o'yinimiz go'libi bo'ldi! 🥳")
    else:
        print(f"Har ikkala ishtirokchi ham {count1}ta harf topdi va Durrang!! 🙃")

    while True:
        answer = input("yana o'ynashni hohlaysizmi? (yes/no) >> ").lower()
        if answer == "yes":
            game1()
        else:
            break


def game1():
    quation = input("1 kishilik o'ynashni tanlaysizmi yoki 2 kishilikmi (1/2) >> ")
    if quation == "1":
        play1()
    elif quation == "2":
        play2()
    else:
        print("Bunday kiritiluvchi yo'q! 😕")
        


game1()