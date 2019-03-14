from fonctions import sigmoide, tangente

# tuto : https://www.youtube.com/watch?v=Dso6nQNGrrw&list=PLjyc6gCk4VU3whCnowAFbVfiBpztCpOKL&index=11
# réseau complet, chaque neurone de la couche n sont conneté avec tous les neurones de la couche n+1

class Reseau:
    def __init__(self, name="Unknown", learn="sigmoide", error=0.001):

        """
         On initialise le réseau avec pour parametres :
            - un nom
            - la fonction d'activation voulu au début
            - l'erreur déclarée lors des phases d'apprentissage
        """

        self.name = name
        if "tangente" == str.lower(learn):
            self.fun_learn = tangente
            self.name_fun_learn = "tangente"
        else:
            self.fun_learn = sigmoide
            self.name_fun_learn = "sigmoide"

        self.error = error
        self.couche = []  # tableau de couches avec le nombre de neurones par couche
        self.link = []  # Le tableau avec tout les poids / Synapse
        self.values = []  # le tableau avec les différentes valeurs des neurones
        self.control = 0  # controlleur pour empecher l'ajout de neuron es/couches

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_error(self, nbr):
        if (nbr >0):
            self.error = nbr

    def get_error(self):
        return self.error

    def set_fun_learn(self, name):
        if str.lower(name) == "tangente":
            self.fun_learn = tangente
            self.name_fun_learn = "tangente"

        else:
            self.fun_learn = sigmoide
            self.name_fun_learn = "sigmoide"

    def get_name_fun_learn(self):
        return self.name_fun_learn

    def get_data(self):
        return (self.get_name(), self.get_name_fun_learn(), self.get_error(), self.get_nbr_couche())

    def get_nbr_couche(self):
        return len(self.couche)

    def get_last_couche(self):
        return self.values[-1]

    def set_couche(self, value=2):
        """
            On initialise les différentes couches du réseau
            On a au minimum 2 couoches : entrée + sortie
        """
        if (self.control == 0):
            if value >= 2:
                for i in range(0, value):
                    self.couche.append(0)
            else:
                print("Il doit y avoir au moins 2 couches")

        else:
            print("Le réseau est deja créé, vous en pouvez plus le modifier")

    def add_couche(self, pos):
        """
            Fonction pour ajouter une couche
        """
        if self.control == 0:
            if pos >= 0 and pos < (self.couche):
                self.couche.insert(pos, 0)
            else:
                print("Vous pouvez ajouter une couche dans l'intervale [0," + str(len(self.couche)) + "]")
        else:
            print("Le réseau est deja créé, vous en pouvez plus le modifier")

    def add_neurone(self, couche, nbr=1):
        """
            Ajouter au moins un neurone dans la couche voulue
        """
        if self.control == 0:
            if couche >= 0 and couche <= len(self.couche) - 1 and nbr > 0:
                self.couche[couche] += nbr
        else:
            print("Le réseau est deja créé, vous en pouvez plus le modifier")

    def add_all_neurone(self, tab):
        """
            Pour ajouter tous les neurones d'un seul coup
        """
        if self.control == 0:
            if len(tab) == len(self.couche):
                for i in range(0, len(tab)):
                    self.add_neurone(i, tab[i])
            else:
                print("Le tableau doit etre de taille" + str(len(self.couche)))
        else:
            print("Le réseau est deja créé, vous en pouvez plus le modifier")

    def create_reseau(self):
        """
            On initialise toures les connections entre les neurones
            Les poids sont mis à 0.5 pars défaut
            On initialise aussi le tableau des valeurs des neurones à 0
        """
        test = True
        for j in range(0, len(self.couche)):
            if self.couche[j] <= 0:
                print("La couche ", j, " doit contenir au moins 1 neurone")
                test = False

        if test:
            if self.control == 0:
                self.control = 1
                for i in range(0, len(self.couche)):
                    add = []
                    add1 = []
                    add_values = []
                    for j in range(0, self.couche[i]):
                        if i != len(self.couche) - 1:
                            for k in range(0, self.couche[i + 1]):
                                add1.append(0.5)
                            add.append(add1)
                            add1 = []
                        add_values.append(0)
                    if i != len(self.couche) - 1:
                        self.link.append(add)
                    self.values.append(add_values)
                else:
                    print("Reseau deja initialisé")
            else:
                print("Le réseau est deja créé, vous en pouvez plus le modifier")

    def parcourir(self, tab):
        """
            Fonction de parcour du réseau
            En parametre les données a tester
        """
        if self.control == 1:
            if len(tab) == self.couche[0]:
                for i in range(0, len(tab)):
                    # On stock dans la 1er couche les donnée entrées :
                    self.values[0][i] = tab[i]
                for i in range(1, len(self.values)):
                    for j in range(0, len(self.values[i])):
                        var = 0
                        for k in range(0, len(self.values[i - 1])):
                            # On stock la somme podérée pour le prochain neurone
                            var += self.values[i - 1][k] * self.link[i - 1][k][j]
                        self.values[i][j] = self.fun_learn(var)
            else:
                print("La couche d'entrée doit contenir ", self.couche[0], "Valeurs")
        else:
            print("Réseau non initialisé")

    def retropropagation(self, tab):
        """
            Fonction de retropropagation par le gradient
            Prend en parametre les données attendu
            La retropropagation ne marche qu'aprés avoir effectué un parcour
        """
        if len(tab) == len(self.values[len(self.values) - 1]):
            for i in range(0, len(tab)):
                # On stock dans la dernière couche la soustraction (valeur_voulue - valeur_obtenue)
                self.values[len(self.values) - 1][i] = tab[i] - self.values[len(self.values) - 1][i]
            # on se balade dans toutes les couches
            for i in range(len(self.values) - 1, 0, -1):
                # mise a jour des poids de la couche sectionné
                for j in range(0, len(self.values[i - 1])):
                    for k in range(0, len(self.link[i - 1][j])):
                        somme = 0
                        for l in range(0, len(self.values[i - 1])):
                            # On effectue la somme pondérée du neurone vers lequel pointe le link
                            somme += self.values[i - 1][l] * self.link[i - 1][j][k]
                        somme = self.fun_learn(somme)

                        # On met à jour le poids de la connexion
                        self.link[i - 1][j][k] -= self.get_error() * (
                                    -1 * self.values[i][k] * somme * (1 - somme) * self.values[i - 1][j])
                # retropropagation de l'erreur
                for j in range(0, len(self.values[i - 1])):
                    somme = 0
                    for k in range(0, len(self.values[i])):
                        # On met à jour les neurones de la prochaine couche en fonction
                        somme += self.values[i][k] * self.link[i - 1][j][k]
                    self.values[i - 1][j] = somme

    def learn(self, entree, sortie):
        """
            Fonction d'apprentissage
            Le premier parametre est l'enssemble de valeurs à tester
            Le second est le resultat attendu
        """
        if self.control == 1:
            if len(entree) == self.couche[0] and len(sortie) == self.couche[len(self.couche) - 1]:
                self.parcourir(entree)
                self.retropropagation(sortie)
            else:
                print("L'entrée doit contenir ", self.couche[0], "valeurs")
                print("La sortie doit contenir", self.couche[len(self.couche) - 1], "valeurs")
        else:
            print("Reseau non initialisé")

    def print_last_couche(self):
        print(self.values[len(self.values) - 1])

    def print_data(self):
        tab = self.get_data()
        print("Nom du réseau :", tab[0],
              "\nFonction d'apprentisage :", tab[1],
              "\nValeur d'erreur d'apprentissage :", tab[2],
              "\nNombre de couche dans le réseau :", tab[3])

    def print_all(self):
        print('Values :')
        self.print_values()
        print("\nLink :")
        self.print_link()

    def print_values(self):
        i = 1
        for each in self.values:
            print("Couche ", i, ":")
            i += 1
            print(each)

    def print_link(self):
        i = 1
        for each in self.link:
            print("Liens ", i, ":")
            i += 1
            for k in each:
                print(k)
            print()

    def print_couche(self):
        print(self.couche)
