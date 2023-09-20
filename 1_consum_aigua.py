#1- Càlcul de la factura de consum de l’aigua
#Escriu un algoritme que permeti a l’usuari calcular el consum d’aigua en un domicili. Calcula la
#factura de l’aigua, donats els litres d’aigua gastats per l’usuari i sabent el següent:
#
#a) Hi ha una quota fixe mensual de 6€ pel servei.
#b) Si el consum és menor de 50 litres, no es paga la quota variable, només el fixe.
#c) Si el consum d’aigua es troba entre 50 i 200 litre es factura el litre a 0.1 €.
#d) Si el consum d’aigua és major a 200 litres es cobra el litre a 0.3 €.
#
#Mostra a l’usuari un menú per consola que permeti calcular l’import de la seva factura en funció
#dels litres d’aigua que ha consumit





consum = int(input("Indica el consum de l'aigua:"))

def exercici_1(consum):
    preu_final = 0.0
    if consum < 50:
        preu_final = 6
    elif consum >= 50 and consum >= 200:
        preu_final = consum * 0.1
    elif consum > 200:
        preu_final = consum * 0.3
    print("La factura es de " + str(preu_final) + "€")

exercici_1(consum)


