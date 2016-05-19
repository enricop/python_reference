####################################
#    FUNZIONI come oggetti
####################################

def add(x,y): return x + y

def subtract(x,y): return x - y

def do_binary_op(op, x, y):
    return op(x, y)

# possiamo riferirci alla funzione 'add' per nome
z = do_binary_op(add, 5, 10) # z = 15

####################################
#    CLOSURES
####################################
def make_printer(msg):
    def printer():
        print(msg)
    return printer

myprinter = make_printer('Foo!')

# l'istanza 'printer' referenzia l'oggetto locale 'msg'.
# la funzione 'printer()' può quindi essere chiamata anche esternamente
# perchè python la tiene in vita nello stack

# la variabile 'msg' è considerata una 'free variable'
# non ne viene fatta una copia locale nella funzaione 'make_printer'
myprinter() # stampa 'Foo!'

####################################
#    Funzioni Lambda
#
# sintassi:   lambda arguments: expression
####################################

double = lambda x: x * 2

print(double(5))

# la funzione filter() prende due argomenti:
# - una funzione
# - una lista sulla quale applicare (obj iterabile)
# e construisce una lista per i valori che ritornano True dalla funzione

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

even_num = list(filter(lambda x: (x%2 == 0) , my_list))
print(even_num)

# la funzione map() prende due argomenti:
# - una funzione
# - una lista sulla quale applicare (obj iterabile)
# e construisce una lista applicando la funzione a tutti gli elementi della lista

doubled = list(map(lambda x: x * 2 , my_list))
print(doubled)

# possiamo dichiarare una funzione in questo modo
is_odd = lambda x: x % 2

# possiamo usare una funzione lambda come sorting key
numbers = [55, 22, 53, 16, 67, 363612, 64361, 12556]
lsB_ordered = sorted(numbers, key=lambda x: x & 0xFF)

####################################
#    Descrittori
####################################

# Attach a new function to an existing object

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

me = Person("Stephen", 27)

def sleep(self):
    if self.age <= 25:
        print("later")
    else:
        print("zzz")

# Bind the sleep method to myself
me.sleep = sleep.__get__(me)
me.sleep() # Prints "zzz"

####################################
#    Decoratori
####################################

def function():
    pass
f = staticmethod(function)

@staticmethod
def f(...):
    pass

#Python has a special syntax that allows you to wrap or "decorate" functions (and classes) at compile time:
#
#The off_by_one function takes a function as it's sole argument and returns a new function.

#We decorated the add function with off_by_one by placing @off_by_one above the function definition. This is equivalent to writing the following after the definition:

def off_by_one(original_function):
    def new_function(x, y):
        return original_function(x, y) + 1
    return new_function

@off_by_one
def add(x, y):
    return x + y



####################################
#    GENERATORI
####################################

# si costruiscono utilizzando l'istruzione 'yield'
# in questo modo i metodi __iter__ e __next__ di un iteratore
# generico sono implementati automaticamente

# in questa funzione il valore di n è ricordato per ogni chiamata
# fino all'ultimo statement yield
def my_gen():
    """a simple generator function"""
    n = 1
    print("This is printed first")
    yield n

    n += 1
    print("This is printed second")
    yield n

    n += 1
    print("This is printed at last")
    yield n

# se questa funzione viene chiamata,
# tutte le volte che ritorna il ciclo for riprenderà dall'indice i
# in cui era rimasto
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        yield my_str[i]

"""
 esempio di generatore su dizionario:
def get_all_records(lookup, keys):
    for key in keys:
        yield datasource.get(key)

for record in get_all_records(lookup, keys):
    print(record)
    """

####################################
#    ITERATORI
####################################
"""Gli iteratori sono un protocollo particolare in python
 che permettono di scorrere un insieme di oggetti dello stesso tipo
 Sono definibili con la parola chiave __iter__

 La funzione next() si può utilizzare per scorrere con l'iteratore l'insieme ordinato"""

with open('/etc/passwd') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')

def reverse_iter(seq):
    position = len(seq) - 1
    while True:
        if position < 0:
            raise StopIteration # questa istruzione è generica dei 'generatori'. termina l'iterazione.
        yield seq[position]
        position -= 1

class BackwardsSequence(list):
    def __iter__(self):
        return reverse_iter(self)

####################################
#    PROTOCOLLI
####################################

#Comparison(__eq__, __gt__, __lt__)
#Containers(__contains__, __setitem__, __getitem__)
#Iterators(__iter__, next)
#Context Managers(__enter__, __exit__)
#Stringification(__str__, __unicode__, __repr__)
#Descriptors(__get__, __set__)
#Instance Creation(__new__, __metaclass__ attribute)
