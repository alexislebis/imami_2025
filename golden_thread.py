##### VARIABLES

ba_A = 3 #nb de A
ba_T = 0 #nb de T
ba_G = 0 #nb de G
ba_C = 1 #nb de C

ratio_AT_GC = (ba_A + ba_T) / (ba_C + ba_G) #float #addition #division

qte_AT, qte_GC = ba_A + ba_T, ba_G + ba_C #Many values to many variables
ratio_AT_GC = qte_AT / qte_GC #abstraction ++ sur le calcul du ratio pour être plus résiliant au changement

brinADN_part1   = "AGGGATC" #string
brinADN_part2   = "TTTGCTA"
brinADN         = brinADN_part1 + brinADN_part2 # concatenation de string ; operation sur les strings

is_brin_malforme = False # or not True # equivalent is_brin_bienforme = True

# typage exemple avec +

##### Interactivité
    ##### Affichage

print("Ceci est un message affiché sur la sortie standard de votre machine")
print("Vous pouvez aller chercher le contenu d'un variable stocké en mémoire vive (RAM) en l'insérant dans un print")
print(brinADN)
print("Vous pouvez afficher plusieurs variables en même temps pour créer des vues plus riches (deux manières de faires)")
print("La fusion du brin", brinADN_part1, "et du brin", brinADN_part2,"donne", brinADN,".")
print(f'La fusion du brin {brinADN_part1} et du brin {brinADN_part2} donne {brinADN}.')
print(f'La fusion du brin {brinADN_part1} et du brin {brinADN_part2} donne {brinADN_part1+brinADN_part2}.')
print("Retour chariot \n et \t pour mise en forme de l'affichage")
print("Vous pouvez aussi afficher des emoji ! 🤖 ☠️ ❤️❤️❤️")

    ##### Interaction avec l'utilisateur
valeurTapee = input("Ceci est le message qui va être demandé avant que le programme n'attende que l'utilisateur rentre quelque chose, stocké ensuite dans la variable valeurTapee")
print(f'On affiche la valeur de la variable : valeurTapee={valeurTapee}')
print("On peut demander un nouveau brin à l'utilisateur maintenant !")
brin_user = input("Merci de renseigner un brin d'ADN")
print("Mais... ne jamais faire confiance à l'utilisateur !")
print(brin_user)
print("Input forcément chaine de caractère")
print("Cast de l'entrée utilisateur")
valeur_entiere = int(brin_user) #ici, on force la chaîne de caractère à devenir un entier