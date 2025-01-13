#!/usr/bin/python3
import sys

# Vérifie si des arguments ont été passés
if len(sys.argv) > 1:
    print("Liste des arguments :")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i}: {arg}")
else:
    print("Aucun argument fourni.")

