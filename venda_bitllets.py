

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
                calcul = 2.20*cost
                print("El preu es de:", calcul)
            case "TCasual":
                calcul = 10.20*cost
                print("El preu es de:", calcul)
            case "TMes":
                calcul = 54.00*cost
                print("El preu es de:", calcul)
            case "TTrimestre":
                calcul = 145.30*cost
                print("El preu es de:", calcul)
            case "TJove":
                calcul = 105.00*cost
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