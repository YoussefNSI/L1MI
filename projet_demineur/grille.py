from random import randint
class Grille:
    def __init__(self):
        """
        Initialisation de la taille du tableau et de son contenu
        """
        self.taille = 16
        self.tableau_jeu = [[0 for i in range(self.taille)]for j in range(self.taille)]

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
    def tableau_mine_init(self):
        """
        Génération des Bombes
        Génération du nombre de Bombe a un point x y (si ce point ne contient pas de bombe)
        """
        nombre_bombes:int = 50
        x:int = 0
        y:int = 0
        unefois:bool = True
        for i in range(nombre_bombes):
            while (self.tableau_jeu[x][y] == -1) or (unefois):
                x = randint(0,self.taille-1)  
                y = randint(0,self.taille-1) 
                unefois = False
            self.tableau_jeu[x][y] = -1
            #Version brute d'addition du nombre de bombes autour
            if (x==0):
                if (y==0):
                    if (self.tableau_jeu[0][1] != -1):
                        self.tableau_jeu[0][1] = self.tableau_jeu[0][1] + 1 
                    if (self.tableau_jeu[1][1] != -1):
                        self.tableau_jeu[1][1] = self.tableau_jeu[1][1] + 1 
                    if (self.tableau_jeu[1][0] != -1):
                        self.tableau_jeu[1][0] = self.tableau_jeu[1][0] + 1 
                elif (y==self.taille-1):
                    if (self.tableau_jeu[1][self.taille-1] != -1):
                        self.tableau_jeu[1][self.taille-1] = self.tableau_jeu[1][self.taille-1] + 1 
                    if (self.tableau_jeu[1][self.taille-2] != -1):
                        self.tableau_jeu[1][self.taille-2] = self.tableau_jeu[1][self.taille-2] + 1 
                    if (self.tableau_jeu[0][self.taille-2] != -1):
                        self.tableau_jeu[0][self.taille-2] = self.tableau_jeu[0][self.taille-2] + 1 
                else:
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
            elif (x == self.taille-1):
                if (y==0):
                    if (self.tableau_jeu[self.taille-1][1] != -1):
                        self.tableau_jeu[self.taille-1][1] = self.tableau_jeu[self.taille-1][1] + 1 
                    if (self.tableau_jeu[self.taille-2][1] != -1):
                        self.tableau_jeu[self.taille-2][1] = self.tableau_jeu[self.taille-2][1] + 1 
                    if (self.tableau_jeu[self.taille-2][0] != -1):
                        self.tableau_jeu[self.taille-2][0] = self.tableau_jeu[self.taille-2][0] + 1 
                elif (y==self.taille-1):
                    if (self.tableau_jeu[self.taille-2][self.taille-1] != -1):
                        self.tableau_jeu[self.taille-2][self.taille-1] = self.tableau_jeu[self.taille-2][self.taille-1] + 1 
                    if (self.tableau_jeu[self.taille-2][self.taille-2] != -1):
                        self.tableau_jeu[self.taille-2][self.taille-2] = self.tableau_jeu[self.taille-2][self.taille-2] + 1 
                    if (self.tableau_jeu[self.taille-1][self.taille-2] != -1):
                        self.tableau_jeu[self.taille-1][self.taille-2] = self.tableau_jeu[0][self.taille-2] + 1 
                else:
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
            elif (y == 0):
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
            elif (y == self.taille-1):
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
            else:
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
            print(x, " ", y, " ", i)
            unefois = True

def verification(Tab):
    """
    Permet de vérifier si le tableau est bien crée avec 50 bombes.
    Arguement :
        Tab : Argument de type Grille.
    Return : rien .
    Print: affiche le nombre de bombes dans la console.
    """
    compteur:int = 0
    for i in range(Tab.taille):
        for j in range(Tab.taille):
            if (Tab.tableau_jeu[i][j] == -1):
                compteur = compteur + 1
    print(compteur)    


Reponse = Grille()
Reponse.affichage()
Reponse.tableau_mine_init()
Reponse.affichage()
