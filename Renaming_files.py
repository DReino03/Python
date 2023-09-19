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
            
            

    
