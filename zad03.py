"""
Utwórz skrypt, która pobierze od użytkownika odpowiedzi na pytania – ankieta z pytaniami jak w
przykładzie (pytania 1-7) oraz pytaniem o imię i nazwisko:
https://www.webankieta.pl/wzor-ankiety/ankieta-czytelnicza/
"""


print("Ankieta czytelnicza")
p0="Jak masz na imię i nazwisko? "
print(p0)
answ0 = input()

p1="Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie ... ?  "
print(p1)
n1= int(input  ("Wybierz odpowiedź spośród : 1-oglądanie telewizji/filmów/seriali 2-czytanie książek/czasopism 3-słuchanie muzyki,4-inny"))

if   n1 == 1:
    answ1=("oglądanie telewizji/filmów/seriali ")
elif n1 == 2:
    answ1=("czytanie książek/czasopism")
elif n1 == 3:
    answ1=("słuchanie muzyki")
else :
    answ1 = input()

p2="W jakich okolicznościach czytasz książki najczęściej? "
print(p2)
n2= int(input  ("Wybierz odpowiedź spośród : 1-podczas podróży,2-podczas pracy/nauki (to ich element), 3-w ogóle nie czytam,4-inny"))

if   n2 == 1:
    answ2=("podczas podróży ")
elif n2 == 2:
    answ2=("w czasie wolnym (po pracy, na urlopie) ")
elif n2 == 3:
    answ2=("w ogóle nie czytam")
else :
    answ2=input()


p3=("Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru? ")
print(p3)
n3= int(input  ("Wybierz odpowiedź spośród : 1-chęć poszerzenia wiedzy,2-czytanie mnie relaksuje/odpręża, 3-fakt, że czytanie jest modne,4-inny"))
if n3 == 1 :
    answ3 = "chęć poszerzenia wiedzy"
elif n3 == 2 :
    answ3 = "czytanie mnie relaksuje/odpręża"
elif n3 == 3 :
    answ3 = "fakt, że czytanie jest modne"
else :
    answ3=input()


print("Dziękujemy za udział w ankiecie!")

print("---------------------------------\n")
print ("pytanie: ",p0)
print ("odpowiedź: ",answ0)
print ("pytanie: ",p1)
print ("odpowiedź: ",answ1)
print ("pytanie: ",p2)
print ("odpowiedź: ",answ2)
print ("pytanie: ",p3)
print ("odpowiedź: ",answ3)