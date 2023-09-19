#4- Proporció àuria
#Donada la imatge de l’espiral d’or de proporció àuria següent, desenvolupa un algoritme recursiu
#que retorni qualsevol element de la sèrie:
#
#Veient la imatge anterior, se’n desprèn que correspon a una successió de valors determinada
#per una funció. Per exemple, l’element 1 de la successió que correspon al quadrat on hi ha el
#primer punt al centre de l’espiral, per tant f(1), és igual a 1, l’element 2 de la successió és també
#1 i l’element 3 de la successió val 2.
#
#Una altra manera de graficar-ho és de la següent manera:
#
#Com podeu veure a la gràfica, el nombre de quadradets d’ample i alt, correspon al valor de la
#successió.
#
#Així doncs:
#- f(1) = 1
#- f(2) = 1
#- f(3) = 2
#- f(4) = 3
#- ...
#
#
#El programa ha d’oferir una interacció I/O per consola amb l’usuari i que aquest pugui escollir
#quants elements de la sèrie àuria vol visualitzar.
#Si l’usuari escriu un 4, el programa li hauria de retornar 1, 1, 2, 3 que correspon als 4 primers
#elements de la sèrie. Com a extra, podeu permetre a l’usuari escollir un interval d’elements de la
#successió a visualitzar. Així doncs, si escriu (2, 4), l’algoritme li retornarà 1, 2, 3, 5 que correspon
#a 4 elements de la successió començant des del segon element.

def  fibonacci(n):

	if n == 1  or n == 0:
		return n
	else:
		return fibonacci(n-2) + fibonacci(n - 1)

numero = int(input("Indica un numero: "))

if numero < 0:
	print("Prueba otra vez")

i = 0

print("sèrie àuria: ")

for i in range(0, numero):
	print(fibonacci(i))
