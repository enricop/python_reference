from copy import copy

# posso importare una classe dal modulo 'object_oriented'
from .object_oriented import Array

ciao = Array()
#################################
# Integer, Float, Complex
#################################
a = 5
b = 5.0
c = 5 + 3j

"""
prefissi per numeri:
    Binary	'0b' or '0B'
    Octal	'0o' or '0O'
    Hexadecimal	'0x' or '0X'
"""

import fractions
fractions.Fraction(1.5)

import math
math.cos(math.pi)
math.exp(10)
math.log10(1000)
math.sinh(1)
math.factorial(6)

#################################
# List
#################################

# lista vuota
my_list = []

# interi
my_list1 = [1, 2, 3]

# lista innestata
n_list = ["Happy", [2,0,1,5]]
n_list[0][1] # carattere 'a'

# accedere gli elementi in un range
my_list2 = ['p','r','o','g','r','a','m','i','z']
my_list2[5:]

a = [0, 0, 0, 0, 0] # crea lista
b = a               # in python l'operazione di assegnamento imposta un nome all'oggetto 'b'
                    # causa la variabile 'b' a riferirsi allo stesso oggetto della variabile 'a'

a.append(3)         # estende la lista con un sesto elemento 3

c = copy(a)         # il contenuto della lista 'a' è copiato in un nuovo oggetto 'c'

x = 57
a[0] = x            # questo elemento della lista si riferisce a x
a[1] = x            # questo elemento della lista si riferisce a x

"""
metodi:
append(x)	Add item x at the end of the list
extend(L)	Add all items in given list L to the end
insert(i, x)	Insert item x at position i
remove(x)	Remove first item that is equal to x, from the list
pop([i])	Remove and return item at position i (last item if i is not provided)
clear()	Remove all items and empty the list
index(x)	Return index of first item that is equal to x
count(x)	Return the number of items that is equal to x
sort()	Sort items in a list in ascending order
reverse()	Reverse the order of items in a list
copy()	Return a shallow copy of the list

"""

# creare liste con il metodo seguente:
# expressione + for + statement
pow2 = [2 ** x for x in range(10)]

# expressione + for + statement + if
pow2 = [2 ** x for x in range(10) if x > 5]

"""
funzioni builtin:
all()	Return True if all elements of the list are true (or if the list is empty).
any()	Return True if any element of the list is true. If the list is empty, return False.
enumerate()	Return an enumerate object. It contains the index and value of all the items of list as a tuple.
len()	Return the length (the number of items) in the list.
list()	Convert an iterable (tuple, string, set, dictionary) to a list.
max()	Return the largest item in the list.
min()	Return the smallest item in the list
sorted()	Return a new sorted list (does not sort the list itself).
sum()	Return the sum of all elements in the list.
"""

#################################
# Tuple
#################################

# le tuple sono oggetti simili alle liste, ma sono immutabili

# vuota
my_tuple = ()
# interi
my_tuple = (1, 2, 3)
# tipi misti
my_tuple = (1, "Hello", 3.4)
# nested
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
# unpacking di tuple, assegna la tupla esistente di 3 oggetti alle 3 variabili
a, b, c = my_tuple

birth_year = ('Stephen', 1984) # Le tuple sono immutabili
#birth_year[1] = 1341 # Questa istruzione genera un eccezione

"""
metodi:
count(x)	Return the number of items that is equal to x
index(x)	Return index of first item that is equal to x"
"""

"""
funzioni builtin
all()	Return True if all elements of the tuple are true (or if the tuple is empty).
any()	Return True if any element of the tuple is true. If the tuple is empty, return False.
enumerate()	Return an enumerate object. It contains the index and value of all the items of tuple as pairs.
len()	Return the length (the number of items) in the tuple.
max()	Return the largest item in the tuple.
min()	Return the smallest item in the tuple
sorted()	Take elements in the tuple and return a new sorted list (does not sort the tuple itself).
sum()	Retrun the sum of all elements in the tuple.
tuple()	Convert an iterable (list, string, set, dictionary) to a tuple.
"""

# Uso delle tuple
def shout(message="Ciao"):
    print("%s!", message)

shout() # stampa "Ciao"
shout("I love python") #passa primo parametro
shout(message="And keyword arguments") #specifica nome parametro

def takes_all(required, *args, **kwargs):
    # tupla ordinata di tutti gli argomenti
    print(args)

    # dizionario di tutti gli argomenti
    print(kwargs)

"""
un vantaggio delle tuple rispetto alle liste è che possono essere usate
come chiave per un dizionario
"""

#################################
# Stringhe
#################################

# le stringhe sono oggetti immutabili

index = 0
fruit = "ciliegia"
while index < len(fruit): # len() calcola la lunghezza
    print(fruit[index])
    index = index + 1

#################################
# Set
#################################
# insieme non ordinato di oggetti

my_set = {1, 3, 4, 5, 6}
my_set = {1.0, "Hello", (1, 2, 3)}

#il set non può avere elementi modificabili come le liste al suo interno
my_set = {1, 2, [3, 4]} # non valido

#posso costruire un set da una lista:
set([1,2,3,2]) # {1, 2, 3}

"""
metodi:

add()	Add an element to a set
clear()	Remove all elemets form a set
copy()	Return a shallow copy of a set
difference()	Return the difference of two or more sets as a new set
difference_update()	Remove all elements of another set from this set
discard()	Remove an element from set if it is a member. (Do nothing if the element is not in set)
intersection()	Return the intersection of two sets as a new set
intersection_update()	Update the set with the intersection of itself and another
isdisjoint()	Return True if two sets have a null intersection
issubset()	Return True if another set contains this set
issuperset()	Return True if this set contains another set
pop()	Remove and return an arbitary set element. Raise KeyError if the set is empty
remove()	Remove an element from a set. It the element is not a member, raise a KeyError
symmetric_difference()	Return the symmetric difference of two sets as a new set
symmetric_difference_update()	Update a set with the symmetric difference of itself and another
union()	Return the union of sets in a new set
update()	Update a set with the union of itself and others
"""

"""
funzioni:
all()	Return True if all elements of the set are true (or if the set is empty).
any()	Return True if any element of the set is true. If the set is empty, return False.
enumerate()	Return an enumerate object. It contains the index and value of all the items of set as a pair.
len()	Return the length (the number of items) in the set.
max()	Return the largest item in the set.
min()	Return the smallest item in the set.
sorted()	Return a new sorted list from elements in the set(does not sort the set itself).
sum()	Retrun the sum of all elements in the set.
"""

# una alternativa è il frozenset, un set che non può essere mutato

A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

A.isdisjoint(B)
A.difference(B)

frozenset({1, 2, 3, 4, 5, 6})
#A.add(3)
#AttributeError: 'frozenset' object has no attribute 'add'

#################################
# Dizionari
#################################
# I dizionari sono un mappa (chiave, valore)
# L'insieme non è ordinato

my_dict = {'name': 'John', 1: [2, 4, 3]} # tipi misti come chiave e valore
my_dict = dict({1:'apple', 2:'ball'}) # usando la funzione dict()
my_dict = dict([(1,'apple'), (2,'ball')]) # da una sequenza di coppie


music = {"Aidan": "Beats", "Justin": "Grunge"}
music['Stephen'] = 'Sarcasm' # aggiunge una coppia chiave: valore al dizionario

for key in music:
  print("%s=%s", (key, music[key])) # stampa coppia chiave=valore

for value in music.values():
  print("???=%s",value)     #stampa tutti i valori

for (k, v) in music.items():
  print("%s=%s", (k, v))    # stampa coppia chiave=valore

"""
metodi:
clear()	Remove all items form the dictionary.
copy()	Return a shallow copy of the dictionary.
fromkeys(seq[, v])	Return a new dictionary with keys from seq and value equal to v (defaults to None).
get(key[,d])	Return the value of key. If key doesnot exit, return d (defaults to None).
items()	Return a new view of the dictionary's items (key, value).
keys()	Return a new view of the dictionary's keys.
pop(key[,d])	Remove the item with key and return its value or d if key is not found. If d is not provided and key is not found, raises KeyError.
popitem()	Remove and return an arbitary item (key, value). Raises KeyError if the dictionary is empty.
setdefault(key[,d])	If key is in the dictionary, return its value. If not, insert key with a value of d and return d (defaults to None).
update([other])	Update the dictionary with the key/value pairs from other, overwriting existing keys.
values()	Return a new view of the dictionary's values
"""

# creare nuovi dizionari con un iterable

squares = {x: x*x for x in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

"""
builtin:
all()	Return True if all keys of the dictionary are true (or if the dictionary is empty).
any()	Return True if any key of the dictionary is true. If the dictionary is empty, return False.
len()	Return the length (the number of items) in the dictionary.
cmp()	Compares items of two dictionaries.
sorted()	Return a new sorted list of keys in the dictionary.
"""