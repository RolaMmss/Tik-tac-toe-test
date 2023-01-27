
#----------------------------------------------------------------------------------
def afficher_grille(grille:list):
    """_summary_
    Cette fonction doit créer et afficher une grille vide
    Args:
        board (list): represente une grille vide de trois lignes et trois colonnes
    """
    print("    1   2   3 \n")
    print("1   " + grille[0][0] + " | " + grille[0][1] + " | " + grille[0][2])
    print("   ---+---+---")
    print("2   " + grille[1][0] + " | " + grille[1][1] + " | " + grille[1][2])
    print("   ---+---+---")
    print("3   " + grille[2][0] + " | " + grille[2][1] + " | " + grille[2][2] + "\n")
#------------------------------------------------------------------------------
def vérifier_ligne(grille,ligne):
    """
    Cette fonction vérifie si le joueur a placé trois marques sur la ligne sélectionnée
    Args:
        grille (list)
        ligne (int)

    Returns:
        Booleen
    """
    return (grille[ligne][0] == grille[ligne][1] == grille[ligne][2] and grille[ligne][1] != "#")
#------------------------------------------------------------------
def vérifier_colonne(grille,colonne):
    """
    Cette fonction vérifie si le joueur a placé trois marques sur la colonne sélectionnée
    Args:
        grille (list)
        colonne (int)

    Returns:
        Booleen
    """
    return (grille[0][colonne] == grille[1][colonne] == grille[2][colonne] and grille[0][colonne] != "#")
#------------------------------------------------------------------
def vérifier_diagonale(grille):
    """
    Cette fonction vérifie si le joueur a placé trois marques sur l'un des diagonales
    Args:
        grille (list)

    Returns:
        Booleen
    """
    return ((grille[0][0] == grille[1][1] == grille[2][2] and grille[0][0] != "#") or (grille[0][2] == grille[1][1] == grille[2][0] and grille[0][2] != "#") )
#------------------------------------------------------------------
def grille_pleine(grille):
    """_summary_
    cette fonction vérifie si il existe encore des cases vides

    Args:
        grille (list)

    Returns:
        Booleen
    """
    for elt in grille:
        if "#" in elt:
            return False
    return True
#------------------------------------------------------------------
def jouer_un_coup(grille,coup,joueurs):
    """_summary_
    Jouer un coup
      - vérifier si un coup est possible c.à.d :
          * Si la case est vide
          * Si la case existe

    Args:
        grille (list): une grille de trois lignes et trois colonnes
        joueur (str): 2 joueurs indépendants
        coup (int): Si pair alors c'est joueur 1, sinon c'est joueur 2
    """
    while True:
        if coup%2 ==0:      # coup est pair alors joueur 1 joue
            print("C'est le tour de ",joueurs[0])
            ligne = input("Entrez le numéro de ligne : ")
            ligne = int(ligne)
            if (ligne < 1) or (ligne >3) or (isinstance(ligne, float)==True):
                print("Merci d'enter un nombre entier entre 1 et 3")
            colonne = input("Entrez le numéro de colonne : ")
            colonne = int(colonne)
            if  (colonne <1) or (colonne >3) or (isinstance(colonne, float)==True):
                print("Merci d'enter un nombre entier entre 1 et 3")
        else:               # coup est pair alors joueur 2 joue
            print("C'est le tour de ",joueurs[1])
            ligne = input("Entrez le numéro de ligne : ")
            ligne = int(ligne)
            if (ligne < 1) or (ligne >3) or (ligne != int):
                print("Merci d'enter un nombre entier entre 1 et 3")
            colonne = input("Entrez le numéro de colonne : ")
            colonne = int(colonne)
            if  (colonne <1) or (colonne >3) or (colonne != int):
                print("Merci d'enter un nombre entier entre 1 et 3")
        if grille[ligne-1][colonne-1]!= "#":
            print("Merci de choissir une case vide")
        else: 
            return (ligne-1,colonne-1)

# jouer_un_coup(ma_grille)
#------------------------------------------------------------------
def grille_gagnante(grille:list):
    """_summary_

    Args:
        grille (list): _description_
    """
    for i in range(3):
        if vérifier_ligne(grille,i):
            print("ligne gagnante")
            return True
        if vérifier_colonne(grille,i):
            print("colonne gagnante")
            return True
    if vérifier_diagonale(grille):
        print("diagonale gagnante")
        return True
    return False
#---------------------------------------------------------------------

def main():

    ma_grille = [["#","#","#"],["#","#","#"],["#","#","#"]]       
    J1=input("Le pseudo de joueur 1 : ")
    J2=input("Le pseudo de joueur 2 : ")
    joueurs=[J1,J2]    
    coup=1

    while not grille_pleine(ma_grille):
        afficher_grille(ma_grille)
        ligne , colonne = jouer_un_coup(ma_grille,coup,joueurs)
        if coup%2 ==0:      # coup est pair alors joueur 1 joue
            ma_grille[ligne][colonne]= "X"
        else: 
            ma_grille[ligne][colonne]= "O"
        if grille_gagnante(ma_grille):
            afficher_grille(ma_grille)
            print(f"{joueurs[0]} a gagné !" if coup %2 ==0 else "{joueurs[1]} a gagné")
            break
        coup += 1
    else:
        afficher_grille(ma_grille)
        print("Egalité")
main()

        

