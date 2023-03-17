"""
Utwórz 3 zmienne wskazujące na ten sam obiekt – napis „ Python 2023”.
a. Wyświetl wartość logiczną zwróconą przez porównanie napisów ze zmiennej pierwszej i drugiej
oraz drugiej i trzeciej.
b. Wyświetl typy tych zmiennych oraz ich adres w pamięci ( w postaci szesnastkowej – funkcja
hex() )
Pod trzecią zmienną przypisz napis „Java 11”
Ponownie wykonaj podpunkt a i b
"""
import sys
napis = "Python 2023"
a = b = c = napis


ab = False
bc = False
if (a == b):
  ab = True;
if (c == b):
 bc = True;

print("a==b ", str(ab))
print("c==b ", str(bc))

print("a: ",type(a)," b: ", type(b)," c: ",type(c))
print("a: ", hex(id(a)), " b: ", hex(id(b)), " c: ", hex(id(c)))

c = "Java 11"
print ( "a: " , type(a) , " b: " , type(b) , " c: " , type(c))
print ( "a: ", hex(id(a)) , " b: " , hex(id(b)) , " c: " , hex(id(c)))
