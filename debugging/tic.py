def print_board(board):
    """Affiche le plateau de jeu."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """Vérifie si un joueur a gagné."""
    # Vérifie les lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérifie les colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérifie les diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def is_board_full(board):
    """Vérifie si le plateau est plein (match nul)."""
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    """Logique principale du jeu de tic-tac-toe."""
    board = [[" "]*3 for _ in range(3)]  # Plateau vide
    player = "X"  # Le premier joueur commence avec "X"

    while True:
        print_board(board)
        try:
            # Demande les coordonnées du joueur
            row = int(input(f"Entrez la ligne (0, 1 ou 2) pour le joueur {player}: "))
            col = int(input(f"Entrez la colonne (0, 1 ou 2) pour le joueur {player}: "))

            # Vérifie si les coordonnées sont valides
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Indices hors limites. Veuillez réessayer.")
                continue

            # Vérifie si la case est libre
            if board[row][col] != " ":
                print("Cette case est déjà prise ! Essayez une autre.")
                continue

            # Place le symbole du joueur sur le plateau
            board[row][col] = player

            # Vérifie si le joueur actuel a gagné
            if check_winner(board):
                print_board(board)
                print(f"Le joueur {player} a gagné !")
                break

            # Vérifie si le plateau est plein (match nul)
            if is_board_full(board):
                print_board(board)
                print("Match nul !")
                break

            # Change de joueur
            player = "O" if player == "X" else "X"

        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entre 0 et 2.")
            continue


# Lancement du jeu
tic_tac_toe()
