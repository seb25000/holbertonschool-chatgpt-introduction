#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule le factoriel d'un nombre entier non négatif n.
    """
    if n == 0:
        return 1
    elif n > 0:
        return n * factorial(n-1)
    else:
        raise ValueError("Le nombre doit être un entier non négatif.")

if __name__ == "__main__":
    # Vérifier que l'utilisateur a fourni un argument
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <nombre_entier>")
        sys.exit(1)

    try:
        # Convertir l'argument en entier
        num = int(sys.argv[1])

        # Vérifier que l'entier est non négatif
        if num < 0:
            raise ValueError("Le nombre doit être un entier non négatif.")

        # Calculer le factoriel
        f = factorial(num)

        # Afficher le résultat
        print(f"Le factoriel de {num} est {f}.")

    except ValueError as e:
        print(f"Erreur : {e}")
        sys.exit(1)

