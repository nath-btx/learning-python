from array import array

t = array('i', [10,25,31,57,42,94,30,78,12,75,63])

def somme(tab):
    somme = 0
    for i in range (0,len(tab)):
        somme += tab[i]
    return somme


def min(tab):
    min = tab[1]
    for i in range (0,len(tab)):
        if min > tab[i]:
            min = tab[i]
    
    return min

def existe(tab, k):
    for i in range (0,len(tab)):
        if t[i] == k:
            return True
    return False

def sommePairs(tab):
    somme = 0

    for i in range(0,len(tab)):
        if (tab[i]%2 == 0):
            somme += tab[i]

    return somme


def estTrie(tab):

    for i in range (1,len(tab) - 1):
        temp = tab[0]
        if (tab[i] > tab[i+1]):
            return False
    return True

def permutation(tab):
    temp = tab[len(tab) - 1]
    for i in range(0,len(tab) - 1):
        tab[len(tab) - i - 1] = tab[len(tab) - i - 2]
    tab[0] = temp
    return tab


def miroir(tab):
    for i in range(0,int(len(tab)/2)):
        temp = tab[i]
        tab[i] = tab[len(tab) - 1 - i]
        tab[len(tab) - 1 - i] = temp 
    return tab 


print(somme(t))
print(min(t))
print(existe(t, 25))
print(existe(t, 100))
print(sommePairs(t))
print(estTrie(t))
tableau = array('i', [0,1,2,3,4,5,6,7])
print(estTrie(tableau))
print(permutation(t))
print(miroir(t))


