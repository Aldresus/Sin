import random as rng
tableau=["","","","","","","","",""]
symboleJoueur=[]
affiTableau=[]
noms=[]
varVictoire=1
solutionPossible = []
bonneSolution = []

def testSolutionPossible():
    global tableau
    solutionPossible=[]
    for i in range(0,len(tableau)):
        if tableau[i] == "":
            solutionPossible.append(i)
    return solutionPossible

def debutDuJeu():
    global noms
    global symboleJoueur
    J1=input("Nom du J1 ?")
    J2="L'ordinatateur"
    noms=[J1,J2]

    if rng.randint(1,2) == 1:
        print("{0} jouera les X et {1} jouera les O !".format(J1,J2))
        symboleJoueur=["X","O"]
    else:
        print("{0} jouera les O et {1} jouera les X !".format(J1,J2))
        symboleJoueur=["O","X"]
    return J1,J2


def affichage(tableau):
    affiTableau.clear()
    for i in range(1,10):

        if tableau[i-1] =="":
            affiTableau.append("{0}".format(i))
        else:
            affiTableau.append(tableau[i-1])

    print("{0}|{1}|{2}".format(affiTableau[0],affiTableau[1],affiTableau[2]))
    print("{0}|{1}|{2}".format(affiTableau[3],affiTableau[4],affiTableau[5]))
    print("{0}|{1}|{2}".format(affiTableau[6],affiTableau[7],affiTableau[8]))

def choixDeJeuIa(Joueur):
    global tableau
    global noms
    global symboleJoueur
    solutionPossible = []
    bonneSolution = []

    emplacement1Possible=True
    if Joueur==J1:
        while emplacement1Possible:

            emplacementJeu=int(input("Où voulez-vous jouer ? Entrez un des numéro restant ! "))

            if tableau[emplacementJeu-1] != "":
                print("Emplacement déja prit !")
            else:
                emplacement1Possible=False

    else:

        listeEmplacementJeu,numOtreJoueur=ordi700iq(Joueur,symboleJoueur)

        if len(listeEmplacementJeu) > 1:
            emplacementJeu=listeEmplacementJeu[rng.randint(0,len(listeEmplacementJeu)-1)]

        elif len(listeEmplacementJeu) == 0:
            joueurAutre=noms[numOtreJoueur]
            listeEmplacementJeu,trucUseless=ordi700iq(joueurAutre,symboleJoueur)

            if len(listeEmplacementJeu)==0:
                if tableau[4]=='':
                    emplacementJeu=4

                else:
                    solutionPossible=testSolutionPossible()
                    rng.shuffle(solutionPossible)
                    emplacementJeu=solutionPossible[0]

            else:
                if len(listeEmplacementJeu) > 1:
                    numEmplacementJeu=rng.randint(0,len(listeEmplacementJeu)-1)
                    emplacementJeu=listeEmplacementJeu[numEmplacementJeu]
                else:
                    emplacementJeu=listeEmplacementJeu[0]
        else:
            emplacementJeu=listeEmplacementJeu[0]

    if Joueur == J1:
        tableau[emplacementJeu-1]=symboleJoueur[0]
    else:
        tableau[emplacementJeu]=symboleJoueur[1]

def choixDeJeu(Joueur,symboleJoueur):
    global tableau

    emplacement1Possible=True
    while emplacement1Possible:

        emplacementJeu=int(input("Où voulez-vous jouer ? Entrez un des numéro restant ! "))

        if tableau[emplacementJeu-1] != "":
            print("Emplacement déja prit !")
        else:
            emplacement1Possible=False
    if Joueur == J1:
        tableau[emplacementJeu-1]=symboleJoueur[0]
    else:
        tableau[emplacementJeu-1]=symboleJoueur[1]

def victoire(Joueur,symboleJoueur):
    global tableau
    numJoueur=0
    varVictoire=1
    if Joueur == J1:
        numJoueur=0
    else:
        numJoueur=1

    for i in range(0,3):

        if [symboleJoueur[numJoueur],symboleJoueur[numJoueur],symboleJoueur[numJoueur]] == [tableau[0+3*i],tableau[1+3*i],tableau[2+3*i]]:
            print("Victoire de {0}".format(Joueur))
            varVictoire=0

        if [symboleJoueur[numJoueur],symboleJoueur[numJoueur],symboleJoueur[numJoueur]] == [tableau[0+1*i],tableau[3+1*i],tableau[6+1*i]]:
            print("Victoire de {0}".format(Joueur))
            varVictoire=0

    if [symboleJoueur[numJoueur],symboleJoueur[numJoueur],symboleJoueur[numJoueur]] == [tableau[0],tableau[4],tableau[8]] or [symboleJoueur[numJoueur],symboleJoueur[numJoueur],symboleJoueur[numJoueur]] == [tableau[6],tableau[4],tableau[2]] :
        print("Victoire de {0}".format(Joueur))
        varVictoire=0

    if varVictoire != 0:
        if "" not in tableau:
            print("Match nul !")
            varVictoire=0

    return varVictoire

def ordi700iq(Joueur,symboleJoueur):
    global tableau
    varVictoire=1
    solutionPossible=testSolutionPossible()
    tableauTest = tableau.copy()
    bonneSolution=[]
    if Joueur == J1:
        numJoueur=0
        numOtreJoueur=1
    else:
        numJoueur=1
        numOtreJoueur=0

    for j in solutionPossible:
        tableauTest = tableau.copy()
        tableauTest[j]=symboleJoueur[numJoueur]
        for i in range(0,3):
            if [symboleJoueur[numJoueur],symboleJoueur[numJoueur],symboleJoueur[numJoueur]] == [tableauTest[0+3*i],tableauTest[1+3*i],tableauTest[2+3*i]]:
                varVictoire=0
                bonneSolution.append(j)

            if [symboleJoueur[numJoueur],symboleJoueur[numJoueur],symboleJoueur[numJoueur]] == [tableauTest[0+1*i],tableauTest[3+1*i],tableauTest[6+1*i]]:

                varVictoire=0
                bonneSolution.append(j)

        if [symboleJoueur[numJoueur],symboleJoueur[numJoueur],symboleJoueur[numJoueur]] == [tableauTest[0],tableauTest[4],tableauTest[8]] or [symboleJoueur[numJoueur],symboleJoueur[numJoueur],symboleJoueur[numJoueur]] == [tableauTest[6],tableauTest[4],tableauTest[2]] :
            varVictoire=0
            bonneSolution.append(j)

    return bonneSolution, numOtreJoueur


J1,J2=debutDuJeu()
affichage(tableau)
while varVictoire:
    for i in range(0,2):
        print("Au tour de {0}".format(noms[i]))
        choixDeJeuIa(noms[i])
        varVictoire=victoire(noms[i],symboleJoueur)
        affichage(tableau)
        if varVictoire == 0:
            break


