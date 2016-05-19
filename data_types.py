from copy import copy

# posso importare una classe dal modulo 'object_oriented'
from .object_oriented import Array

ciao = Array()

#################################
# Stringhe
#################################
# le stringhe sono oggetti immutabili

a = [0, 0, 0, 0, 0] # crea lista
b = a               # in python l'operazione di l'assegnamento copia imposta un nome all'oggetto 'b'
                    # causa la variabile 'b' a riferirsi allo stesso oggetto della variabile 'a'

a.append(3)         # estende la lista con un sesto elemento

x = 57
a[0] = x            # questo elemento della lista si riferisce a x
a[1] = x            # questo elemento della lista si riferisce a x

index = 0
fruit = "ciliegia"
while index < len(fruit): # len() calcola la lunghezza
    print(fruit[index])
    index = index + 1

c = copy(a)         # il contenuto della lista 'a' è copiato in un nuovo oggetto 'c'

#################################
# Dizionari
#################################
# I dizionari sono un mappa (chiave, valore)
music = {"Aidan": "Beats", "Justin": "Grunge"}
music['Stephen'] = 'Sarcasm' # aggiunge una coppia chiave: valore al dizionario

for key in music:
  print("%s=%s", (key, music[key])) # stampa coppia chiave=valore

for value in music.values():
  print("???=%s",value)     #stampa tutti i valori

for (k, v) in music.items():
  print("%s=%s", (k, v))    # stampa coppia chiave=valore

#################################
# Tuple
#################################
birth_year = ('Stephen', 1984) # Le tuple sono immutabili
#birth_year[1] = 1341 # Questa istruzione genera un eccezione

# Uso delle tuple
def shout(message="Ciao"):
    print("%s!", message)

shout() # stampa "Ciao"
shout("I love python") #passa primo parametro
shout(message="And keyword arguments") #specifica nome parametro

def takes_all(required, *args, **kwargs):
    # tuple of all positional (non-keyword) arguments
    print(args)

    # dictionary of all keyword arguments
    print(kwargs)


Python Numbers
Python List
Python Tuple
Python String
Python Set
Python Dictionary