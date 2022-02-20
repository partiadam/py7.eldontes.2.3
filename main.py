'''
2.3 Feladat
A program tároljon el egy szót egy változóban. A felhasználó adjon meg egy betűt, amiről a program döntse el, hogy előfordul-e a szóban! Az eredményről tájékoztassa a felhasználót, és írja ki a tárolt szót is!

A felhasználónak többször is legyen lehetősége újabb tippet megadnia. A bekérés addig folytatódjon, amíg a felhasználó nem ad meg betűt, csupán egy ENTER-t üt!

Igyekezz minél felhasználóbarátabbá tenni a programot! A programnak lehetnek egyéb hasznos funkciói, például gyűjtheti és kiírhatja a jó és a rossz tippeket (betűket).
'''

eltalalta = []
nemtalaltael = []
szo = 'mindenható'


while True:
    felhasznalo = input('Adj meg egy betűt: ')
    if felhasznalo in szo:
        print('Eltaláltad!')
        eltalalta.append(felhasznalo)
        print(eltalalta)
    else:
        print('Nem találtad el!')
        nemtalaltael.append(felhasznalo)
        print(nemtalaltael)
    if felhasznalo == '':
        break
    
    
print('A szó:',szo)