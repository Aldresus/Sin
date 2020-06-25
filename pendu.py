from random import randint
#6 vies
vies=6
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
    print(affichageMotJoueur)
    return(affichageMotJoueur)






motADeviner=motATrouver()
affichageJoueur=affichageMot(motADeviner)

while vies > 0:
    changeLettre=[]
    temp1=""
    perteVies=0
    lettre=input("à quelle lettre pensez-vous ?").lower()
    
    print("première lettre mot =",motADeviner[0])
    print("motADeviner=",motADeviner)
    print("longeur mot=",len(motADeviner))
    print("longeur affichage=",len(affichageJoueur))

    for i in range(len(motADeviner)):
        print("i=",i)

        if lettre==motADeviner[i]:
            print("lettre juste",lettre)
            changeLettre.append(lettre)

        else:
            print("affichage joueur=",affichageJoueur[i])
            changeLettre.append(affichageJoueur[i])
            perteVies+=1

    print("pertieVies=",perteVies)
    if perteVies==len(motADeviner):
        
        print("Vous perdez une vie !")
        vies-=1
        print("il vous en reste {0}".format(vies))
        
            

    print("changelettre=",changeLettre)
    
    affichageJoueur=temp1.join(changeLettre)
    print("temp1=",temp1)
    print("affichagejoueur",affichageJoueur)