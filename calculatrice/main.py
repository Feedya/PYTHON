#------------------------------------------------------------------------------------------
#CALCULATOR
#le : str apres expression c est pour dire le type de variable
#le -> c est quelle valeur la fonction va renvoie
def calculer(expression: str) -> float:
    #replace(ancien, nouveau)
    expr = expression.replace(" ", "")

    if expr == "":
        #la c est comme un throw en cpp
        raise ValueError("vide")

    if "(" in expr or ")" in expr:
        raise ValueError("parenthese interdit")

    #un set en python est un type de variable
    #elle ne peut pas avoir de douublons, et n est pas indexable
    #dans notre cas comme on lui donne une string il va decouper charactere par charactere
    operateurs_valides: set = set("+-*/")

    # les [] c est une liste
    nombres = []
    operateurs = []
    #le tampon va nous servir de juste voir si notre calculs se finit bien par un nombre
    tampon = ""

    #----------------------------------------------------------------
    #verification de se qu on a ecrit comme calculs
    #le tampon va nous servir dans le cas si notre calculs se finit par un operator
    for caractere in expr:
        # si nombre
        if caractere.isdigit() or caractere == ".":
            tampon += caractere
        #si operators
        elif caractere in operateurs_valides:
            if tampon == "":
                raise ValueError("ca commence par operator, c est faux")
            #on prend le nombre
            nombres.append(float(tampon))
            #on prend l operator
            operateurs.append(caractere)
            tampon = ""
        else:
            raise ValueError("Cas cheloux qui normalement devrait pas arriver")
    #si ca se finit par un operator
    if tampon == "":
        raise ValueError("bomboclat un operator a la fin")
    nombres.append(float(tampon))

    for val in nombres:
        if val < 0:
            raise ValueError("pas de negatifs")
    #----------------------------------------------------------------
    #calculs
    nombres_filtres = [nombres[0]]
    operateurs_filtres = []

    #-----------------------------------------------------------------------------------------------------
    #premierement on fait les multiplication et division
    # enumerate nous permet de prendre l index et l elements qui se trouve a cette index
    #i = index
    #op = elements
    for i, op in enumerate(operateurs):
        valeur_suivante = nombres[i + 1]

        if op == "*":
            nombres_filtres[-1] = nombres_filtres[-1] * valeur_suivante
        elif op == "/":
            #si on divise par 0
            if valeur_suivante == 0:
                raise ZeroDivisionError(" 0 ou rien?")
            nombres_filtres[-1] = nombres_filtres[-1] / valeur_suivante
        else:
            operateurs_filtres.append(op)
            nombres_filtres.append(valeur_suivante)
    #------------------------------------------------------------------------------------------------------
    #apres on faut les + et -
    resultat = nombres_filtres[0]
    for i, op in enumerate(operateurs_filtres):
        valeur_suivante = nombres_filtres[i + 1]
        if op == "+":
            resultat += valeur_suivante
        elif op == "-":
            resultat -= valeur_suivante
            #if resultat < 0:
            #   raise ValueError("resultats negatifs meme si c est pas faux en sois")
    #----------------------------------------------------------------

    return resultat
#------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------
#MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN
if __name__ == "__main__":
    #les print en python mettent tous seul les \n
    print("Fedor calculator")
    #on va calculer en boucle pour sortir de la calculatrice faut ecrire "fin"
    print("pour sortir du calculator faut ecrire 'fin'")
    while True:
        #input vas prendre se qu on ecrit dans le terminal jusqu a un '\n'
        entree = input("\nmathematique > ")
        if entree.strip().lower() == "fin":
            print("aurevoir")
            break
        try:
            res = calculer(entree)
            print(f"Resultat : {res}")
        except Exception as err:
            print(f"Erreur : {err}")
#----------------------------------------------------------------------------------
