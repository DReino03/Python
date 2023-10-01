#2- Màquina de venda de bitllets de metro
#Els objectius d’aquest exercici són:
#• Treballar estructures condicionals
#• Treballar estructures iteratives
#• Implementar estructures de control d’input de dades
#
#Hem d’implementar una màquina de venda de bitllets de transport metropolità.
#
#En primer lloc la màquina ofereix diferents títols de transport que poden ser adquirits, l’usuari
#només pot escollir una opció d’aquesta llista:
#o Bitllet senzill
#o TCasual
#o TMes
#o TTrimestre
#o TJove
#
#Un cop l’usuari hagi escollit una opció se li preguntarà les zones que vol viatjar.(1,2 o 3).

#Un cop escollides les zones es mostrarà el preu i l’usuari podrà introduir els diners (només es
#pot pagar en efectiu, amb monedes i bitllets d’EURO existents).
#
#Els preus son els següents:
#
#o Bitllet senzill............2,20€ (1a zona)
#o TCasual.................10,20€ (1a zona)
#o TMes......................54,00€ (1a zona)
#o TTrimestre..........145,30€ (1a zona)
#o TJove...................105,00€ (1a zona)
#
#Els preus per la segona zona son els preus de la primera zona multiplicats per 1,35.
#
#Els preus de la tercera zona son els preus de la primera zona multiplicats per 1,89.
#
#Un cop pagat el bitllet es retornarà el canvi i la màquina quedarà altre cop en disposició de
#vendre un nou bitllet.
#
def exercici_2_billet():

    exit = False
    while exit == False:

        billet = input("Indica el billet que vols seleccionar:")
        zona = int(input("Indica quantes zones:"))

        cost = 0

        if zona == 1:
            cost = 1.0
        elif zona == 2:
            cost = 1.35
        elif zona == 3:
            cost = 1.89
    
 match billet:
            case "Bitllet senzill":
                calcul = 2.40*cost
                print("El preu es de:", calcul)
            case "TCasual":
                calcul =  11.35*cost
                print("El preu es de:", calcul)
            case "TMes":
                calcul = 20.00*cost
                print("El preu es de:", calcul)
            case "TTrimestre":
                calcul = 145.30*cost
                print("El preu es de:", calcul)
            case "TJove":
                calcul = 40.00*cost
                print("El preu es de:", calcul)


        pagament = int(input("Indica la quantitat de diners per a pagar: "))       
        print("Retornant canvi de:",pagament-calcul)

        tancament = input(str("Vols retirar un altre bitllet? Y/N:"))
        if tancament == "Y":
            exit = False
        elif tancament == "N":
            exit = True
            print("Fins la proxima!")    

exercici_2_billet()
