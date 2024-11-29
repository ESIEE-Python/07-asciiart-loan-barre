"""
C'est a moi
"""
#### Imports et définition des variables globales


#### Fonctions secondaires
import sys
sys. setrecursionlimit(20000)

def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne 
    de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici
    if not s:
        return []

    c = [s[0]]
    nb = [1]

    for i in range(1, len(s)):
        if s[i]==s[i-1]:
            nb[-1]+=1
        else:
            c.append(s[i])
            nb.append(1)

    return list(zip(c, nb))


def artcode_r(s):
    """retourne la liste de tuples encodant une 
    chaîne de caractères passée en argument selon un algorithme 
    récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici
    # Cas de base : chaîne vide ou d'un seul caractère


    # Trouver combien de fois le premier caractère se répète


    # Appel récursif sur la sous-chaîne restante

    # cas de base
    if not s:
        return []
    if len(s) == 1:
        return [(s[0], 1)]

    # recherche nombre de caractères identiques au premier
    count = 1
    while count < len(s) and s[count] == s[0]:
        count += 1

    # appel récursif
    return [(s[0], count)] + artcode_r(s[count:])


#### Fonction principale


def main():
    """
    Permet l'appel des fonctions secondaires
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
