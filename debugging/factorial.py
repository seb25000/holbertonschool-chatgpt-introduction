#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1 # Ajout de cette ligne
    return result

if len(sys.argv) > 1: # Ajout de cette ligne
    try:
      f = factorial(int(sys.argv[1]))
      print(f)
    except ValueError:
      print("Veuillez entrer un nombre entier valide comme argument.")
else: # Ajout de cette ligne
    print("Veuillez fournir un argument entier.")
