case_vide = " "

plateau = [case_vide for _ in range(9)]

joueurs = ("X", "O")
joueur = joueurs[0]

placeholder = ("1","2","3","4","5","6","7","8","9")
""
#Affiche le plateau de jeu.

def afficher_plateau():
    print(" ----+----+----")
    for i in range(9):
        print("|", plateau[i] if plateau[i] != case_vide else placeholder[i], end=" ")
        if i % 3 == 2:
            print("|")
            print(" ----+----+----")



def victoire(board, signe):
    return (
        board[0] == board[1] == board[2] == signe or#ligne
        board[3] == board[4] == board[5] == signe or
        board[6] == board[7] == board[8] == signe or
        board[0] == board[3] == board[6] == signe or#colone 
        board[1] == board[4] == board[7] == signe or
        board[2] == board[5] == board[8] == signe or
        board[0] == board[4] == board[8] == signe or#diagonal
        board[2] == board[4] == board[6] == signe)
#Vérifie si un joueur a gagné la partie avec les colonnes, lignes ou diagonales.

# Vérifie si le plateau est plein.
def plateau_plein(board):
    return case_vide not in board #verifie avec true 

#minamax

def ordinateur(board, signe):
    coups = [i for i in range(9) if board[i] == case_vide]

    for i in coups:
        copie = board[:]
        copie[i] = signe
        if victoire(copie, signe):
            return i# pour bloquer ladversaire et dessayer de gagner au tour suivant 

    adv = "O" if signe == "X" else "X"#deteemine l'adversaire 
    for i in coups:
        copie = board[:]
        copie[i] = adv
        if victoire(copie, adv):#pour quil essaye de gagner au tour suivant
            return i

    import random
    if coups:
        return random.choice(coups)
    return False#si aucun coup possible 


# Choix du mode de jeu 

mode = int(input("Tapez 1 pour jouer avec l'IA, 2 pour jouer contre un autre joueur : "))


while True:
    afficher_plateau()

    choix = -1
    while choix not in range(9) or plateau[choix] != case_vide:
        try:
            choix = int(input("Choisissez une case (1-9) : ")) - 1
            if choix not in range(9):
                print("Veuillez entrer un nombre entre 1 et 9.")
            elif plateau[choix] != case_vide:
                print("Cette case est déjà occupée.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    plateau[choix] = joueur

    if victoire(plateau, joueur):
        afficher_plateau()
        print(f"Vous avez gagné — joueur : {joueur}")
        break#dit qui a gagner 

    if plateau_plein(plateau):
        afficher_plateau()
        print("Match nul.")
        break#dit match nul si personne a gagner 


# mode ia 
    
    if mode == 1:
        ia = ordinateur(plateau, "O")
        plateau[ia] = "O"
        print(f"minimax joue en case {ia+1}")

        if victoire(plateau, "O"):
            afficher_plateau()
            print("minimax gagne la partie.")
            break


# mode joueur vs joueur

    else:
        choix2 = -1
        while choix2 not in range(9) or plateau[choix2] != case_vide:
            try:
                choix2 = int(input("Joueur O, choisissez une case (1-9) : ")) - 1
                if choix2 not in range(9):
                    print("Veuillez entrer un nombre entre 1 et 9.")
                elif plateau[choix2] != case_vide:
                    print("Cette case est déjà occupée.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")

        plateau[choix2] = "O" #pour autre joueur marque O pour son tour

        if victoire(plateau, "O"):# si joueur O gagne affiche et quitte
            afficher_plateau()
            print("Le joueur O gagne la partie.")
            break 
