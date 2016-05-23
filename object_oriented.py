#==============================================
# Esempio di classe con attributo e sottoclassi
#============================   ==================

class LoudTalker(object):
    # qui aggiungo un attributo della classe di nome "suffix"
    # l'attributo può essere referenziato attraverso:
    #   -l'oggetto della classe (LoudTalker.suffix)
    #   -l'istanza della classe (self.suffix)
    suffix = "!"

    def say(self, message):
        print("%s%s" % (message, self.suffix))

class SubLoudTalker(LoudTalker):
    pass

assert SubLoudTalker.suffix == "!"

class UnsureTalker(LoudTalker):
    suffix = "..." # fa l'ovverride dell'attributo di LoudTalker ad un nuovo valore

pensively = UnsureTalker()
pensively.say("I'm pretty sure")

# e' possibile l'ereditarietà multipla
class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass

# e' possibile l'ereditarietà multilivello
class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Derived1):
    pass

#=============================================
# Esempio di classe base con inizializzazione
# e reimplementazione di metodi 'speciali'
#=============================================

class Array(object):
    # il metodo __init__ è chiamato alla creazione dell'oggetto
    # effettivamente questo metodo è un "inizializzatore"
    # il metodo __new__ è il reale costruttore della classe
    # ma di solito viene implementato ed usato solo nelle metaclassi
    def __init__(self, length = 0, baseIndex = 0):
        assert length >= 0
        self._data = [ None for i in range(length) ] #crea una lista di elementi tutti a None
        self._baseIndex = baseIndex # limite inferiore per gli indici

    # implementa metodo __copy__ nel caso si usi la funzione python 'copy()'
    # per copiare un oggetto di tipo Array
    def __copy__(self):
        result = Array(len(self._data))
        for i, datum in enumerate(self._data):
            result._data[i] = datum
        result._baseIndex = self._baseIndex
        return result

    # ...
    def getOffset(self, index):
        offset = index - self._baseIndex
        if offset < 0 or offset >= len(self._data):
            raise IndexError
        return offset

    def __getitem__(self, index):
        return self._data[self.getOffset(index)]

    def __setitem__(self, index, value):
        self._data[self.getOffset(index)] = value

#=============================================
# Esempio di classe astratta (solo python 3)
#=============================================

import abc

"""Una classe astratta può contenere uno o più metodi astratti,
 Può essere usata come classe base per una derivata.
 Non può essere istanziata.
 si può fornire comunque nelle classi astratte una implementazione dei metodi,
 che le sottoclassi possono utilizzare con super().
 I metodi astratti devono essere implementati dalle classi 'concrete' derivate
 Questa classe astratta estende la classe __builtin__.object """
class AbstractTalker(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """ permette polimorfismo
          in questo caso possiamo riferirci alla classe Parent senza conoscere il suo nome
          possiamo risalire così la gerarchia delle classi e chiamare i metodi delle classi parent """

        super(AbstractTalker, self).__init__()  # permette di riferirsi all'oggetto/istanza parent ed
                                        # usare il suo metodo __init__()
        # avrei potuto scrivere:
        # object.__init__(self)

    """ controlla la gerarchia degli oggetti/classi
        posso usare anche il metodo "issubclass() """
    def compara(self, obj):
        if isinstance(self, obj.__class__): # controlla se 'self' è istanza della classe di obj
            pass
        elif isinstance(obj, self.__class__): # controlla se 'obj' è istanza della classe di self
            pass
        else:
            return (self.__class__.__name__ == obj.__class__.__name__)

    @abc.abstractmethod
    def format(self, message):
        return message # oppure: raise NotImplementedError

    def say(self, message):
        print(self.format(message))

# defininiamo in queste classi derivate l'implementazione dei metodi
class LoudTalker(AbstractTalker):
    def format(self, message):
        return "%s!" % message

class Screamer(LoudTalker):
    def format(self, message):
        return super(Screamer, self).format(message).upper()

# esempio di ereditarietà multipla, con classe astratta
class ShoutFormatterMixin(object):
    def format(self, message):
        return "%s!" % message

class PublicAddressSystem(ShoutFormatterMixin, AbstractTalker):
    def play_music(self, song):
        super(PublicAddressSystem, self).say(song.tablature)

#=============================================
# Esempio di namespace delle variabili
#=============================================
def outer_function():
    a = 20

    def inner_function():
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)

a = 10
outer_function()
print('a =', a)

## stampa:
# a = 30
# a = 20
# a = 10

def outer_function():
    global a
    a = 20

    def inner_function():
        global a
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)

a = 10
outer_function()
print('a =', a)

## stampa:
# a = 30
# a = 30
# a = 30

#=============================================
# Overloading di operatore __add__
#=============================================
class Point:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

p1 = Point(2,3)
p2 = Point(-1,2)
print(p1 + p2)
# stampa (1,5)

#=============================================
# PROPRIETÀ
#=============================================

# Proprietà:
# sono un modo comodo ed elegante per esporre attributi della classe

"""
    property() è una funzione builtin che ritorna un oggetto di tipo property

    ha la seguente signature:
    property(fget=None, fset=None, fdel=None, doc=None)

    - un esempio:
    temperature = property(get_temperature,set_temperature)

    - altro esempio con funzioni lambda:
    data = property(
        fget = lambda self: self.getData())
    baseIndex = property(
        fget = lambda self: self.getBaseIndex(),
        fset = lambda self, value: self.setBaseIndex(value))
"""

# si possono definire proprietà in sola lettura
# si possono definire proprietà in lettura/struttura

class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature,set_temperature)

# un secondo modo di definire le proprietà della classe
# è usare il decoratore @property e setter in questo modo

class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value