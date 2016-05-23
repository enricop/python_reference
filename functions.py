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
#    Metodi Statici e Metodi di Classi
####################################

class Pizza(object):
    def __init__(self, ingredients):
        self.ingredients = ingredients

    # il metodo statico non dipende dal fatto che la classe sia istanziata
    # il metodo statico non deve dipendere da alcun attributo interno alla classe
    # 'Pizza().mix_ingredients is Pizza.mix_ingredients' ritorna True

    @staticmethod
    def mix_ingredients(x, y):
        return x + y

    # il metodo di classo non dipende dall'oggetto in se ma dalla classe a cui è legato
    # è molto simile al metodo statico ma permette di referenziare al suo interno in
    # modo dinamico il nome delle classe e i suoi attributi
    # 'Pizza.get_radius is Pizza().get_radius' ritorna True
    # posso usare il parametro 'cls' al posto di 'self'

    @classmethod
    def from_fridge(cls, fridge):
        return cls(fridge.get_cheese() + fridge.get_vegetables())

    radius = 42
    @classmethod
    def get_radius(cls):
        return cls.radius

    def cook(self):
        return self.mix_ingredients(self.cheese, self.vegetables)

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

"""Le funzioni e i metodi sono chiamati 'callable'
In fatti ciascun oggetto che implementa il metodo speciale __call__ è tale
Un decoratore è un 'callable' che ritorna un 'callable' aggiungendo o modificando
funzionalità di esso"""

# make_pretty è un decoratore
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

ordinary()
#stampa:
#I am ordinary

pretty = make_pretty(ordinary)
pretty() #l'oggetto callable pretty è stato decorato

#stampa:
#I got decorated
#I am ordinary

#### Invece di fare l'assegnamento nella penultima riga è possibile #####
@make_pretty
def ordinary():
    print("I am ordinary")

# che ottiene lo stesso effetto che:
def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)

#######################################
#   DECORATORI CONCATENATI
#######################################
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)

"""stampa (l'ordine di scrittura del decoratore è importante):

******************************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Hello
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
******************************

"""

#######################################
#   DECORATORI DI FUNZIONI CON PARAMETRI FISSI
#######################################
def smart_divide(func):
    def inner(a,b):
        print("I am going to divide",a,"and",b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a,b)    # quando si ritorna la funzione decorata vanno rispettati i parametri
    return inner

@smart_divide
def divide(a,b):
    return a/b

#######################################
#   DECORATORI DI FUNZIONI CON PARAMETRI VARIABILI
#######################################

"""un esempio di decoratore parametri variabili:

 possiamo riferirci ai parametri di qualsiasi funzione passata in ingresso
 siccome 'args' è una serie di tuple con i nomi degli argomenti ordinati
 e 'kwargs' è il dizionario con i valori per ciascun argomento
"""
def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner

####################################
#    GENERATORI
####################################

"""si costruiscono utilizzando l'istruzione 'yield'
 in questo modo i metodi __iter__ e __next__ di un iteratore
 generico sono implementati automaticamente

 in questa funzione il valore di n è ricordato per ogni chiamata
 fino all'ultimo statement yield
 """
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

 La funzione next() si può utilizzare per scorrere con l'iteratore l'insieme ordinato
 """

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


def function():
    pass
f = staticmethod(function)

@staticmethod
def f(...):
    pass