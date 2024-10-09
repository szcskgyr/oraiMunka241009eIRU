from beolvas import *
from random import *

def egyAlap():
    # 1.	A program olvasson be a konzolról egy egész számot! A program döntse el, hogy a megadott szám páros vagy páratlan, és írja ki az eredményt a konzolra!
    szam1 = beolvasEgesz()

    if szam1%2 == 1:
        print("páratlan")
    else:
        print("páros")

def egyAlapA():
    # a. Ugyanezt valósítsd meg véletlen számmal is!
    szam1 = randint(-10, 10)
    print(szam1)
    if szam1%2 == 1:
        print("páratlan")
    else:
        print("páros")

def egyAlapB():
    # b. Csak páros számot fogadj el, és add meg a négyzetét!
    szam1 = randint(-10, 10)
    # print("szám: "+str(szam1))
    while not(szam1%2 == 0):
        szam1 = randint(-10, 10)
        # print("új szám: "+str(szam1))
    print("szám négyzete: "+str(szam1**2))

def egyAlapC():
    # c. Alakítsd át a b programot, hogy függvényel működjön!
    szam1 = generalParosEgesz()
    print("szám négyzete: " + str(szam1 ** 2))

def kettoAlap():
    # 2. A program  olvasson be a konzolról egy egész számot! Ha a szám 1 és 12 közötti, akkor legyen a beolvasott szám egy hónap sorszáma! A program írja ki a konzolra a sorszámmal megadott hónap nevét! Hiba (1-nél kisebb vagy 12-nél nagyobb szám) esetén legyen hibaüzenet!
    szam1 = beolvasEgesz()
    if (szam1>=1) and (szam1 <= 12):
        if szam1 == 1:
            print("január")
        elif szam1 == 2:
            print("február")
        elif szam1 == 3:
            print("március")
        elif szam1 == 4:
            print("április")
        elif szam1 == 5:
            print("május")
        elif szam1 == 6:
            print("június")
        elif szam1 == 7:
            print("július")
        elif szam1 == 8:
            print("augusztus")
        elif szam1 == 9:
            print("szeptember")
        elif szam1 == 10:
            print("október")
        elif szam1 == 11:
            print("november")
        else:
            print("december")
    else:
        print("Hiba: nem megfelelő szám!")

def kettoAlapA():
    # a. Egy véletlen szám (1 és 12 között) alapján írasd ki az eredményt!
    # szam1 = randint(1, 12)  # csak jó
    szam1 = randint(-5, 15)  # kevés rossz
    # szam1 = randint(-100,100) # sok rossz
    print("hónap sorszáma: "+str(szam1))
    if (szam1>=1) and (szam1 <= 12):
        if szam1 == 1:
            print("január")
        elif szam1 == 2:
            print("február")
        elif szam1 == 3:
            print("március")
        elif szam1 == 4:
            print("április")
        elif szam1 == 5:
            print("május")
        elif szam1 == 6:
            print("június")
        elif szam1 == 7:
            print("július")
        elif szam1 == 8:
            print("augusztus")
        elif szam1 == 9:
            print("szeptember")
        elif szam1 == 10:
            print("október")
        elif szam1 == 11:
            print("november")
        else:
            print("december")
    else:
        print("Hiba: nem megfelelő szám!")

def kettoAlapB():
    # b. Ellenőrzötten csak 1 és 12 közötti számot fogadunk el a bekérés során!