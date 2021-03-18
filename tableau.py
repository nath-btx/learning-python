from array import array

tab = array('i', [1, 3, 5, 7, 9])

for i in range (0,len(tab)):
    print(tab[i])


def somme(tab):
    somme = 0
    for i in range (0,len(tab)):
        somme += tab[i]

    return somme

print("somme : ", somme(tab))