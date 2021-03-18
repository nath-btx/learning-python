print("Saississez la taille des figures")
n = int(input())

def Carre(n):
    Rangee(n)
    Espace(n)
    Rangee(n)

def Etoile():
    print("* ", end='')

def Rangee(n):
    for i in range (0,n):
        Etoile()
    print()

def Espace(n):
    for i in range (0, n-2):
        Etoile()
        for i in range (0, n - 2):
            print("  ", end='')
        Etoile()
        print()
    

def Losange(n):
    Space(n+1)
    Etoile()
    print()
    for i in range(0,n):
        Space(n - i)
        Etoile()
        Space(2 * i + 1)
        Etoile()
        print()
    for i in range (1, n):
        Space(i + 1)
        Etoile()
        Space(2 * n - 2 * i - 1)
        Etoile()
        print()
    Space(n+1)
    Etoile()
    print()

def Space(n):
    for i in range (0,2*n):
        print(" ",end='')

def Cross(n):
    for i in range (0, n):
        Space(i + 1)
        Etoile()
        Space(2 * n - 2 * i - 1)
        Etoile()
        print()
    Space(n+1)
    Etoile()
    print()
    for i in range(0,n):
        Space(n - i)
        Etoile()
        Space(2 * i + 1)
        Etoile()
        print()





Carre(n)
Losange(n)
Cross(n)


