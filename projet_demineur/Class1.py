from random import randint
class Grille:
    
    def __init__(self):
        """
        Initialisation de la taille du tableau et de son contenu
        """
        self.taille:int = 16
        self.tableau_jeu:list = [[0 for i in range(self.taille)]for j in range(self.taille)]
        self.bombes:int = 0

    def tableau_joueur(self):
        self.tableau_jeu:list = [["." for i in range(self.taille)]for j in range(self.taille)]

    def affichage(self):
        """
        Affichage du tableau de jeu
        """
        for i in range(self.taille):
            chaine:str = ""
            for j in range(self.taille):
                chaine = chaine + " " + str(self.tableau_jeu[i][j])
            print(chaine, "\n")
    #Il faudrait ajouter un programme qui charge une map démineur par un fichier.

    def tableau_chargement(self):

        nom_fichier:str = str(input("Comment s'appelle votre fichier? (il doit bien sur être dans le même dossier ) "))
        fic = open(nom_fichier,"r")
        lignes = fic.readlines()
        bombe:bool = False
        Ligne:int = 0
        Colonne:int = 0 
        for ligne in lignes : 
            for e in ligne:
                if not bombe :
                    if e != " " and e !="\n":
                        if e == "-":
                            self.tableau_jeu[Ligne][Colonne] = -1
                            bombe = True
                            Colonne = Colonne + 1
                        else:
                            self.tableau_jeu[Ligne][Colonne] = e
                            Colonne = Colonne + 1
                else:
                    bombe = False
            Ligne = Ligne +1
            Colonne = 0
        fic.close()
        self.bombes=50

    def stockage_tableau(self):
        fic = open("Tableau_jeu.txt","w")
        for i in range(self.taille):
            for j in range(self.taille):
                fic.write(str(self.tableau_jeu[i][j]))
                fic.write(" ")
            fic.write("\n")
        fic.close()
        print("Enregistrement du fichier fait.")
            
    def trouve_bombe(self):
        self.bombes = self.bombes - 1
    def tableau_mine_init(self):
        """
        Génération des Bombes
        Génération du nombre de Bombe a un point x y (si ce point ne contient pas de bombe)
        """
        self.bombes=50
        x:int = 0
        y:int = 0
        unefois:bool = True
        for i in range(self.bombes):
            while (self.tableau_jeu[x][y] == -1) or (unefois):
                x = randint(0,self.taille-1)  
                y = randint(0,self.taille-1) 
                unefois = False
            self.tableau_jeu[x][y] = -1
            #Version brute d'addition du nombre de bombes autour
            if (x==0):
                self.cas_haut(x,y)
            elif (x == self.taille-1):
                self.cas_bas(x,y)
            elif (y == 0):
                self.cas_gauche(x,y)
            elif (y == self.taille-1):
                self.cas_droite(x,y)
            else:
                self.cas_normal(x,y)
            unefois = True
    def cas_coin_haut_gauche(self,x:int,y:int):
        if (self.tableau_jeu[0][1] != -1):
            self.tableau_jeu[0][1] = self.tableau_jeu[0][1] + 1 
        if (self.tableau_jeu[1][1] != -1):
            self.tableau_jeu[1][1] = self.tableau_jeu[1][1] + 1 
        if (self.tableau_jeu[1][0] != -1):
            self.tableau_jeu[1][0] = self.tableau_jeu[1][0] + 1

    def cas_coin_haut_droite(self,x:int,y:int):
        if (self.tableau_jeu[1][self.taille-1] != -1):
            self.tableau_jeu[1][self.taille-1] = self.tableau_jeu[1][self.taille-1] + 1 
        if (self.tableau_jeu[1][self.taille-2] != -1):
            self.tableau_jeu[1][self.taille-2] = self.tableau_jeu[1][self.taille-2] + 1 
        if (self.tableau_jeu[0][self.taille-2] != -1):
            self.tableau_jeu[0][self.taille-2] = self.tableau_jeu[0][self.taille-2] + 1

    def cas_haut_longueur(self,x:int,y:int):
        if (self.tableau_jeu[0][y-1] != -1):
            self.tableau_jeu[0][y-1] = self.tableau_jeu[0][y-1] + 1
        if (self.tableau_jeu[0][y+1] != -1):
            self.tableau_jeu[0][y+1] = self.tableau_jeu[0][y+1] +1
        if (self.tableau_jeu[1][y-1] != -1):
            self.tableau_jeu[1][y-1] = self.tableau_jeu[1][y-1] +1
        if (self.tableau_jeu[1][y] != -1):
            self.tableau_jeu[1][y] = self.tableau_jeu[1][y] +1
        if (self.tableau_jeu[1][y+1] != -1):
            self.tableau_jeu[1][y+1] = self.tableau_jeu[1][y+1] +1
    
    def cas_haut(self,x:int,y:int):
        if (y==0):
            self.cas_coin_haut_gauche(x,y)
        elif (y==self.taille-1):
            self.cas_coin_haut_droite(x,y)
        else:
            self.cas_haut_longueur(x,y)

    def cas_coin_bas_gauche(self,x:int,y:int):
        if (self.tableau_jeu[self.taille-1][1] != -1):
            self.tableau_jeu[self.taille-1][1] = self.tableau_jeu[self.taille-1][1] + 1 
        if (self.tableau_jeu[self.taille-2][1] != -1):
            self.tableau_jeu[self.taille-2][1] = self.tableau_jeu[self.taille-2][1] + 1 
        if (self.tableau_jeu[self.taille-2][0] != -1):
            self.tableau_jeu[self.taille-2][0] = self.tableau_jeu[self.taille-2][0] + 1

    def cas_coin_bas_droite(self,x:int,y:int):
        if (self.tableau_jeu[self.taille-2][self.taille-1] != -1):
            self.tableau_jeu[self.taille-2][self.taille-1] = self.tableau_jeu[self.taille-2][self.taille-1] + 1 
        if (self.tableau_jeu[self.taille-2][self.taille-2] != -1):
            self.tableau_jeu[self.taille-2][self.taille-2] = self.tableau_jeu[self.taille-2][self.taille-2] + 1 
        if (self.tableau_jeu[self.taille-1][self.taille-2] != -1):
            self.tableau_jeu[self.taille-1][self.taille-2] = self.tableau_jeu[0][self.taille-2] + 1

    def cas_bas_longueur(self,x:int,y:int):
        if (self.tableau_jeu[self.taille-1][y-1] != -1):
            self.tableau_jeu[self.taille-1][y-1] = self.tableau_jeu[self.taille-1][y-1] + 1
        if (self.tableau_jeu[self.taille-1][y+1] != -1):
            self.tableau_jeu[self.taille-1][y+1] = self.tableau_jeu[self.taille-1][y+1] +1
        if (self.tableau_jeu[self.taille-2][y-1] != -1):
            self.tableau_jeu[self.taille-2][y-1] = self.tableau_jeu[self.taille-2][y-1] +1
        if (self.tableau_jeu[self.taille-2][y] != -1):
            self.tableau_jeu[self.taille-2][y] = self.tableau_jeu[self.taille-2][y] +1
        if (self.tableau_jeu[self.taille-2][y+1] != -1):
            self.tableau_jeu[self.taille-2][y+1] = self.tableau_jeu[self.taille-2][y+1] +1

    def cas_bas(self,x:int,y:int):
        if (y==0):
            self.cas_coin_bas_gauche(x,y)
        elif (y==self.taille-1):
            self.cas_coin_bas_droite(x,y)
        else:
            self.cas_bas_longueur(x,y)

    def cas_gauche(self,x:int,y:int):
        if (self.tableau_jeu[x-1][y] != -1):
            self.tableau_jeu[x-1][y] = self.tableau_jeu[x-1][y] + 1
        if (self.tableau_jeu[x-1][y+1]!= -1):
            self.tableau_jeu[x-1][y+1] = self.tableau_jeu[x-1][y+1] + 1
        if (self.tableau_jeu[x][y+1] != -1):
            self.tableau_jeu[x][y+1] = self.tableau_jeu[x][y+1] + 1
        if (self.tableau_jeu[x+1][y] != -1):
            self.tableau_jeu[x+1][y] = self.tableau_jeu[x+1][y] + 1
        if (self.tableau_jeu[x+1][y+1] != -1):
            self.tableau_jeu[x+1][y+1] = self.tableau_jeu[x+1][y+1] + 1

    def cas_droite(self,x:int,y:int):
        if (self.tableau_jeu[x-1][self.taille-2] != -1):
            self.tableau_jeu[x-1][self.taille-2] = self.tableau_jeu[x-1][self.taille-2] + 1
        if (self.tableau_jeu[x-1][self.taille-1]!= -1):
            self.tableau_jeu[x-1][self.taille-1] = self.tableau_jeu[x-1][self.taille-1] + 1
        if (self.tableau_jeu[x][self.taille-2] != -1):
            self.tableau_jeu[x][self.taille-2] = self.tableau_jeu[x][self.taille-2] + 1
        if (self.tableau_jeu[x+1][self.taille-2] != -1):
            self.tableau_jeu[x+1][self.taille-2] = self.tableau_jeu[x+1][self.taille-2] + 1
        if (self.tableau_jeu[x+1][self.taille-1] != -1):
            self.tableau_jeu[x+1][self.taille-1] = self.tableau_jeu[x+1][self.taille-1] + 1

    def cas_normal (self,x:int,y:int):
        if(self.tableau_jeu[x-1][y-1] != -1):
            self.tableau_jeu[x-1][y-1] = self.tableau_jeu[x-1][y-1] + 1
        if(self.tableau_jeu[x-1][y] != -1):
            self.tableau_jeu[x-1][y] = self.tableau_jeu[x-1][y] + 1
        if(self.tableau_jeu[x-1][y+1] != -1):
            self.tableau_jeu[x-1][y+1] = self.tableau_jeu[x-1][y+1] + 1
        if(self.tableau_jeu[x][y-1] != -1):
            self.tableau_jeu[x][y-1] = self.tableau_jeu[x][y-1] + 1
        if(self.tableau_jeu[x][y+1] != -1):
            self.tableau_jeu[x][y+1] = self.tableau_jeu[x][y+1] + 1
        if(self.tableau_jeu[x+1][y-1] != -1):
            self.tableau_jeu[x+1][y-1] = self.tableau_jeu[x+1][y-1] + 1
        if(self.tableau_jeu[x+1][y] != -1):
            self.tableau_jeu[x+1][y] = self.tableau_jeu[x+1][y] + 1
        if(self.tableau_jeu[x+1][y+1] != -1):
            self.tableau_jeu[x+1][y+1] = self.tableau_jeu[x+1][y+1] + 1