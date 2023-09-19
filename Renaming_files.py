#3- Renaming files
#L’objectiu d’aquest exercici és el de crear un script que permeti a l’usuari renombrar els noms
#dels arxius d’un determinat directori. Per a tal cosa, se li demanarà la ruta del directori on hi ha
#els arxius a modificar i seguidament el patró de text a buscar pera ser modificar usant
#expressions regulars i finalment el text que volem que s’hi posi enlloc del text actual buscat.
#
#Crea un script python en un fitxer .py per a ésser executat des del terminal de la següent manera:
#py + nomScript.py
#
#Nota: En funció de com hagueu configurat el PATH de la variable d’entorn de l’intèrpret de
#python, per executar un script de python potser heu de fer ús d’una paraula diferent a py.
#
#Aquest script, un cop executat, ha de permetre interacció amb l’usuari a través del terminal de
#manera que se li pregunti a l’usuari a quin directori hi ha els fitxers a renombrar, quin patró de
#text buscar i quin text posar en el seu lloc.
#
#Com podeu imaginar, haureu de crear un bucle que pugui iterar sobre tots els fitxers continguts
#dins de la carpeta que ha demanat l’usuari.
#
#Nota: Us podeu crear un conjunt de fitxers .txt de prova dins del mateix directori per testejar que
#funciona.
import os

def rename_file():
    exit = False
    while exit == True:
            ruta = input(str("Indica la ruta del directori que vols treballar:"))
            # os.chdir lleva a la ruta especificada
            os.chdir(ruta)

            fitxer = input(str("Indica el fitxer que vols modificar el nom:"))
            open(fitxer,"w")

            rename_file = input(str("Indica quin nom vols fer servir"))
                        
            continuacio = input(str("Vols continuar modificant? Y/N"))
            if continuacio == "Y":
                exit = False
            elif continuacio == "N":
                exit = True
            

    
