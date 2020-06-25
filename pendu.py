from random import randint
#6 vies
vies=6
penduAscii=["+———————+\nI       O\nI     / I \ \nI      / \ \nI\n=========","+———————+\nI       O\nI     / I \ \nI      /   \nI\n=========","+———————+\nI       O\nI     / I \ \nI          \nI\n=========","+———————+\nI       O\nI     / I   \nI          \nI\n=========","+———————+\nI       O\nI       I   \nI          \nI\n=========","+———————+\nI       O\nI           \nI          \nI\n=========","+———————+\nI        \nI           \nI          \nI\n========="]

def motATrouver():

    fichierMots=open("dico.txt","r")
    mots=fichierMots.readlines()
    fichierMots.close
    n=len(mots)

    #choix du mot
    motADeviner=mots[randint(0,n-1)].replace("\n","").lower()

    return motADeviner


def affichageMot(motADeviner):
    affichageMotJoueur=""
    #converti le mot en une suite de point de la même longeur (1 pts = 1 lettre)
    for i in range(len(motADeviner)):
        affichageMotJoueur+="."
    print("Le mot est:",affichageMotJoueur)
    return(affichageMotJoueur)

motADeviner=motATrouver()
affichageJoueur=affichageMot(motADeviner)

while vies > 0:
    changeLettre=[]
    temp1=""
    perteVies=0
    choixLettre=True

    while choixLettre:

        lettre=input("à quelle lettre pensez-vous ?").lower()

        if lettre in affichageJoueur:
            print("Vous avez déja trouvé cette lettre !")
        else:
            choixLettre=False

    for i in range(len(motADeviner)):

        if lettre==motADeviner[i]:
            changeLettre.append(lettre)

        else:
            changeLettre.append(affichageJoueur[i])
            perteVies+=1

    if perteVies==len(motADeviner):
        
        print("Vous perdez une vie !")
        vies-=1
        print("{0}".format(penduAscii[vies]))
    
    affichageJoueur=temp1.join(changeLettre)
    print("Le mot est :",affichageJoueur)

    if motADeviner==affichageJoueur:
        print("Vous avez gagné !")
        break

    print("------------------------\n")

if vies==0:
    print("Le mot était: {0} !".format(motADeviner))