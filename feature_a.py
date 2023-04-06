#Broj
import random

from pip._vendor.distlib.compat import raw_input

print("Pogodi broj\n")
zamisljeni_broj = random.randint(0, 100)

ime = raw_input("Unesite vase ime: ")
print("Zdravo {0:s}. \nZamislio sam neki broj od 1 do 100. Da li mozes da pogodis koji je to broj?".format(ime))

pogodio = 0;
while not pogodio:
    print("Unesite broj: ")
    broj = int(raw_input())
    if broj == zamisljeni_broj:
        pogodio = 1
    elif broj > zamisljeni_broj:
        print("Broj koji sam zamislio je manji od {0:d}.".format(broj))
    else:
        print("Broj koji sam zamislio/la je veci od {0:d}.".format(broj))
print("BRAVO! Pogodio si! Zamisljeni broj je {0:d}.".format(zamisljeni_broj))
