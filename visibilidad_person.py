# Publico: nombre
# Protegido: _nombre
# Privado: __nombre

from abc import ABC, abstractmethod


class Person:
    def __init__(self):
        self.__inicializaValores()
        self.__dimeSecreto()

    def setName(self, name):
        self._name = name

    def getName(self):
        self.popular += 1
        return self._name if self.popular < 5 else "No te lo digo"

    def __inicializaValores(self):
        self._name = "PERSONA"
        self.__secreto = "SOLO YO SE ESTO"
        self.popular = 0
        self._x = None

    def __dimeSecreto(self):
        print(f"Solo PERSON puede saber el: {self.__secreto}")


print("PERSONA:--------------------------")

foo = Person()
foo.setName("Luke Skywalker")
print(foo.getName())
print(f"POPULARIDAD: {foo.popular}")
print(foo.getName())
print(foo.getName())
print(foo.getName())
print(foo.getName())
# print(foo.__dimeSecreto())


class PersonaSocial(ABC):
    @abstractmethod
    def saludar(self):
        pass


class Cocinero(Person, PersonaSocial):
    def cocina(self):
        print("Estoy cocinando")

    def describe(self):
        print(f"Soy el cocinero: {self._name}")

    def saludar(self):
        print("El cocinero saluda")


print("COCINERO:--------------------------")
bar = Cocinero()
bar.cocina()
bar.describe()


class PersonaAntiocial(ABC):
    @abstractmethod
    def ignora(self):
        pass


class Ladron(Person, PersonaAntiocial):
    def roba(self):
        print("Estoy robando")

    def espia(self):
        # print(f"El secreto es: {self.__secreto}")
        # self.__dimeSecreto()
        pass

    def ignora(self):
        print("El ladron pasa de todos")


print("LADRON: --------------------------")
bar = Ladron()
bar.roba()
bar.espia()
