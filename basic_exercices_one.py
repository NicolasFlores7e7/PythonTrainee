import os
import re


"""Escriu un algoritme que permeti a l’usuari calcular el consumption d’aigua en un domicili. Calcula la
factura de l’aigua, donats els litres d’aigua gastats per l’usuari i sabent el següent:


a) Hi ha una quota fixe mensual de 6€ pel servei.
b) Si el consumption és menor de 50 litres, no es paga la quota variable, només el fixe.
c) Si el consumption d’aigua es troba entre 50 i 200 litre es factura el litre a 0.1 €.
d) Si el consumption d’aigua és major a 200 litres es cobra el litre a 0.3 €.


Mostra a l’usuari un menú per consola que permeti calcular l’import de la seva factura en funció
dels litres d’aigua que ha consumit"""




def ex1():
    fix = 6
    valid_input = False
    
    while not valid_input:
        try:
            consumption = int(input("Introduce los litros consumidos: "))
            if consumption < 50:
                print(f"El precio de la factura es: {fix}€")
                valid_input = True
            elif 50 <= consumption <= 200:
                print(f"El precio de la factura es: {fix + consumption * 0.1}€")
                valid_input = True
            else:
                print(f"El precio de la factura es: {fix + consumption * 0.3}€")
                valid_input = True
        except ValueError:
            print("Error: Por favor, introduce un número entero válido.")
        
ex1()



"""L’objectiu d’aquest exercici és el de crear un script que permeti a l’usuari renombrar els noms
dels arxius d’un determinat directori. Per a tal cosa, se li demanarà la ruta del directori on hi ha
els arxius a modificar i seguidament el patró de text a buscar pera ser modificar usant
expressions regulars i finalment el text que volem que s’hi posi enlloc del text actual buscat.


Crea un script python en un fitxer .py per a ésser executat des del terminal de la següent manera:
py + nomScript.py"""




def ex3():
   path = input("Introduce la ruta del directorio: ")
   pattern = input("Introduce el patrón de texto a buscar: ")
   new_text = input("Introduce el nuevo texto: ")
   for file in os.listdir(path):
       if re.search(pattern, file):
           new_name = re.sub(pattern, new_text, file)
           os.rename(path + '/' + file, path + '/' + new_name)
           print(f"El archivo {file} ha sido renombrado a {new_name}")


ex3()


"""Donada la imatge de l’espiral d’or de proporció àuria següent, desenvolupa un algoritme recursiu
que retorni qualsevol element de la sèrie:


Veient la imatge anterior, se’n desprèn que correspon a una successió de valors determinada
per una funció. Per exemple, l’element 1 de la successió que correspon al quadrat on hi ha el
primer punt al centre de l’espiral, per tant f(1), és igual a 1, l’element 2 de la successió és també
1 i l’element 3 de la successió val 2.


Una altra manera de graficar-ho és de la següent manera:


Com podeu veure a la gràfica, el nombre de quadradets d’ample i alt, correspon al valor de la
successió.


Així doncs:
- f(1) = 1
- f(2) = 1
- f(3) = 2
- f(4) = 3
- ...
El programa ha d’oferir una interacció I/O per consola amb l’usuari i que aquest pugui escollir
quants elements de la sèrie àuria vol visualitzar.
Si l’usuari escriu un 4, el programa li hauria de retornar 1, 1, 2, 3 que correspon als 4 primers
elements de la sèrie. Com a extra, podeu permetre a l’usuari escollir un interval d’elements de la
successió a visualitzar. Així doncs, si escriu (2, 4), l’algoritme li retornarà 1, 2, 3, 5 que correspon
a 4 elements de la successió començant des del segon element."""




def ex4(n):
   if n == 1 or n == 2:
       return 1
   return ex4(n-1) + ex4(n-2)

valid_input = False

while not valid_input:
    try:
        numbers_to_see = int(input("¿Cuántos números de la serie quieres ver?: "))
        valid_input = True
    except ValueError:
        print("Por favor, introduce un número entero válido.")


for serial_number in range(1, numbers_to_see+1):
   print(ex4(serial_number))



"""Usant un array bidimensional de tipus char, crea el taulell d'escacs en python per tal de que es
mostri a la consola.
Per a fer-ho, has de saber:
• El taulell d'escacs té 8 files i 8 columnes. Un total de 64 caselles.
• Té cel·les blanques i negres de forma alterna.
• La primera casella és blanca i la simbolitzarem amb una 'O'.
• Les caselles negres les car representarem amb la 'X'.
• Les caselles seran blanques quan la suma dels índex de la seva fila i la seva columna
sigui múltiple de 2.
• Els taulells tenen les files numerades de 8 al 1 de dalt a baix.
• Té les columnes numerades de la A a la H d'esquerra a dreta.
• Com que numerarem les files i columnes, necessitarem una fila i una columna extra.


Et proposo que quedi així:


BENVINGUT AL TAULELL D'ESCACS:


O X O X O X O X 8
X O X O X O X O 7
O X O X O X O X 6
X O X O X O X O 5
O X O X O X O X 4
X O X O X O X O 3
O X O X O X O X 2
X O X O X O X O 1
A B C D E F G H


Extra: Dona funcionalitat al taulell d’escacs i permet que s’hi pugui jugar un 1 vs 1 entre dues
persones (no us demanem que programeu IA)."""


def ex5():
   board = [['O' if (i+j) % 2 == 0 else 'X' for i in range(8)] for j in range(8)]
   print("BENVINGUT AL TAULELL D'ESCACS:")
   for i in range(8):
       print(' '.join(board[i]) + f' {8-i}')
   print('A B C D E F G H')

ex5()
