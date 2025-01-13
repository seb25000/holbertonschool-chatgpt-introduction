def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)  # Ajout d'une ligne séparatrice pour l'affichage du plateau


def check_winner(board):
    # Vérifier les lignes
    for row in board:
        if row[0] != " " and row.count(row[0]) == len(row):  # Vérifie que tous les éléments de la ligne sont identiques
            return True

    # Vérifier les colonnes
    for col in range(len(board[0])):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:  # Vérifie les colonnes
            return True

    # Vérifier les diagonales
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]  # Création d'un tableau 3x3
    player = "X"
    move_count = 0  # Compteur de coups joués

    while True:
        print_board(board)

        # Vérifie si le jeu est terminé (victoire ou match nul)
        if check_winner(board):
            print("Félicitations ! Le joueur " + ("O" if player == "X" else "X") + " a gagné !")
            break
        if move_count == 9:  # Vérifie si tous les coups ont été joués (match nul)
            print("Match nul !")
            break

        # Saisie utilisateur avec validation
        while True:
            try:
                row = int(input(f"Entrez la ligne (0, 1 ou 2) pour le joueur {player} : "))
                col = int(input(f"Entrez la colonne (0, 1 ou 2) pour le joueur {player} : "))
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if board[row][col] == " ":  # Vérifie si la case est libre
                        break
                    else:
                        print("Cette case est déjà prise, essayez une autre.")
                else:
                    print("Entrée invalide. Veuillez entrer des valeurs entre 0, 1 ou 2.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre.")

        # Met à jour le plateau avec le coup du joueur
        board[row][col] = player
        move_count += 1

        # Change de joueur
        player = "O" if player == "X" else "X"

    # Affiche le plateau final
    print_board(board)


# Lancement du jeu
tic_tac_toe()

