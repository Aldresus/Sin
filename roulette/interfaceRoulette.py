import tkinter as tk
import sys
from random import randrange
import time

root = tk.Tk()
root.title('JEU DE LA ROULETTE')
nom = tk.LabelFrame(text="JEU DE LA ROULETTE")
frameCagnotte = tk.LabelFrame(text="CAGNOTTE").pack(side="bottom")
nom.pack(fill="both", expand="yes")
messages = tk.StringVar()
messages.set("")

cagnotte=1000
resultats=0


valeurMSG=0
menuDeroulant=[i for i in range (1,37)]

variablePari = tk.IntVar()
variablePari.set(1)

texteAffi = tk.IntVar()
messagesGain = tk.StringVar()
variablePariNombre = tk.IntVar()
variableNombre = tk.IntVar()
textvariable = tk.StringVar()

argent = tk.StringVar()
argent.set("Vous avez{0} $".format(cagnotte))
jeu = True
choix=0

# définition des couleurs
# rouge = [1,3,5,7,9,1,14,16,18,19,21,23,25,27,30,32,34,36]
# noir correspond au complémentaire à 36
# manque correspond aux nombres entre 1 à 18, passe de 19 à 36
# le 0 est la banque.

# on demande quel choix de pari est fait par le joueur et sa mise
# si la mise dépasse la cagnotte on redemande...
def pari():
    global cagnotte
    mise_not_OK = True

    mise = textvariable.get()
    print(mise)

    if mise.isdigit():
        mise=int(mise)
        print(mise)

        if mise > cagnotte:
            print("mise > cagnotte")
            messages.set("Votre mise doit être inférieure à {0}".format(cagnotte))
            root.update_idletasks()

        else:
            mise_not_OK = False
            messages.set("Les jeux sont faits... Rien ne va plus...")
            root.update_idletasks()
            derouleDuJeu(mise)
    else:
        print("mise pas digit")
        messages.set("Vous devez entrer une mise valide !")
        root.update_idletasks()

    return mise

def derouleDuJeu(mise):
    global cagnotte

    choixPossibles=["rouge","noir","pair","impair","passe","manque"]
    bille = roulette()
    choix=variablePari.get()
    if choix < 7:
        choix=choixPossibles[choix]
    else:
        choix=variableNombre.get

    couleur = check_couleur(bille)
    passe_manque = check_manque_passe(bille)
    parite = check_pair_impair(bille)
    resultat = [str(bille),couleur,parite,passe_manque]

    if bille == 0: # la banque gagne tjs sur le zéro
        messages.set("Le résultat est 0, vert : la banque gagne.")
        root.update_idletasks()
    else:
        #print("Le résultat est : ",resultat[0],", ",resultat[1],", ",resultat[2]," et ",resultat[3],".", sep="")
        #print("Le résultat est : %s, %s, %s et %s." %(resultat[0],resultat[1],resultat[2],resultat[3]))
        #print("Le résultat est : {0[0]}, {0[1]}, {0[2]} et {0[3]}.".format(resultat))
        print("Le résultat est : {0}, {1}, {2} et {3}.".format(*resultat))
        if str(choix) in resultat:
            print("Gagné !")
            gain_partie = gain_bis(mise, choix)
            cagnotte = cagnotte + gain_partie
            messagesGain.set("Vous avez gagné {0}, votre cagnotte est de {1}".format(gain_partie,cagnotte))
            argent.set("Vous avez{0} $".format(cagnotte))
            root.update
            print("Vous avez gagné ",gain_partie,".", sep="")

        else:
            cagnotte = cagnotte - mise
            messagesGain.set("Vous avez perdu {0}, votre cagnotte est de {1}".format(mise,cagnotte))
            argent.set("Vous avez{0} $".format(cagnotte))
            root.update
            print("Vous avez perdu ",mise,".", sep="")
    argent.set(cagnotte)
    root.update
    if cagnotte==0:
        messages="Vous êtes ruiné"
        root.update
# gain en rapport avec la mise (on retrouve tjs sa mise si on gagne)
# si on parie sur un nombre : gain = mise * 35
# si on parie sur 18 numéros (Noir-Rouge - Pair-Impair - Manque-Passe) : gain =  mise
def gain(mise, choix):
    choix = str(choix)
    mise = int(mise)
    if (choix == 'pair' or choix == 'impair' or choix == 'rouge' 
            or choix == 'noir' or choix == 'passe' or choix == 'manque'):
        gain = mise * 2
    else:
        gain = mise + mise * 35
    return(gain)

def gain_bis(mise, choix):
    mise = int(mise)
    if choix.isdigit():
        gain = mise + mise * 35
    else:
        gain = mise * 2
    return(gain)

def check_couleur(bille):
    rouge = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    if bille in rouge:
        couleur = 'rouge'
    else:
        couleur = 'noir'
    return(couleur)

def check_manque_passe(bille):
    if bille <= 18:
        passe_manque = 'manque'
    else:
        passe_manque = 'passe'
    return(passe_manque)

def check_pair_impair(bille):
    if bille % 2 == 1:
        parite = 'impair'
    else:
        parite = 'pair'
    return(parite)

# on tire un nombre au hasard entre 0 et 36
def roulette():
    bille = randrange(0,36)
    return(bille)


tk.Label(nom,text="Faites vos jeux !").grid(row= 0,column=0,columnspan=3)
#Pas besoin de commande car ils changent direct la valeur d'une variable--------
rouge = tk.Radiobutton(nom,text="ROUGE",var=variablePari,value=1).grid(row= 1,column=0)
noir = tk.Radiobutton(nom,text="NOIR",var=variablePari,value=2).grid(row= 1,column=1)
pair = tk.Radiobutton(nom,text="PAIR",var=variablePari,value=3).grid(row= 2,column=0)
impair = tk.Radiobutton(nom,text="IMPAIR",var=variablePari,value=4).grid(row= 2,column=1)
passe = tk.Radiobutton(nom,text="PASSE",var=variablePari,value=5).grid(row= 3,column=0)
manque = tk.Radiobutton(nom,text="MANQUE",var=variablePari,value=6).grid(row= 3,column=1)
nombre = tk.Radiobutton(nom,text="NOMBRE",var=variablePari,value=7).grid(row= 5,column=0)
menu = tk.OptionMenu(nom,variableNombre,*menuDeroulant).grid(row= 5,column=1)
#-------------------------------------------------------------------------------

choixmise = tk.Entry(nom,textvariable=textvariable).grid(row= 6,column=1)
textemise = tk.Label(nom,text="MISE :").grid(row= 6,column=0)



argent=tk.Label(frameCagnotte,textvariable=argent).pack(side="top")
affichage=tk.Label(frameCagnotte,textvariable=messages).pack(side="top")
affichageGain=tk.Label(frameCagnotte,textvariable=messagesGain).pack(side="top")

boutonValider = tk.Button(text="Valider !",command=pari).pack(side="top")
quitter = tk.Button(text="QUITTER",command=root.destroy).pack(side="bottom")


root.geometry("260x300")
root.mainloop()

