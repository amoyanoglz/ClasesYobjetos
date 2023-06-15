from random import randint
import datetime
from time import sleep

WAIT = 0.01

class Pato:
    cantidad = 0
    patas = 2
    ultimo_creado = None
    plumas = 0

    def __init__(self, nombre = "Anónimo"):
        self.creado_en = datetime.datetime.now()
        self.nombre = nombre
        self.plumas = randint(1000, 2000)

        print(f"ha nacido el Pato {Pato.cantidad} {self}")

        Pato.cantidad += 1
        Pato.plumas += self.plumas
        Pato.ultimo_creado = self.creado_en

    def __del__(self):
        print(f"ha muerto el Pato {self.nombre}")
        Pato.cantidad -= 1
        Pato.plumas -= self.plumas

    def __str__(self):
        buffer = f"\nPATO:\n"
        buffer += f"   NOMBRE: {self.nombre}\n"
        buffer += f"   CREADO: {self.creado_en}\n"
        buffer += f"   PLUMAS: {self.plumas}\n"

        return buffer

class Perro():
    patas = 4
    def ladra(self):
        print("Guau guau")
    
    def __str__(self):
        return "Perro"

def describe(sobrinos):
    print(f"Donald tiene {len(sobrinos)} sobrinos:")
    for sobrino in sobrinos:
        print(sobrino)

def fiesta_de_patos():
    print("Fiesta de patos")
    festero_1 = Pato()
    festero_2 = Pato()
    sleep(WAIT*4)
    print("Fin de la fiesta")

print("Creando patos...")
sobrinos = []
sobrinos.append(Pato("Jaimito"))
sleep(WAIT)
sobrinos.append(Pato("Jorgito"))
sleep(WAIT)
sobrinos.append(Pato("Juanito"))
sleep(WAIT)

print(f"Hemos creado {Pato.cantidad} patos")
print(f"El último pato creado fue {Pato.ultimo_creado}")
print(f"En total hay {Pato.plumas} plumas")

fiesta_de_patos()

print()
describe(sobrinos)
sleep(WAIT * 6)
indice_al_azar = randint(0, len(sobrinos) - 1)
del(sobrinos[indice_al_azar])
describe(sobrinos)

print(f"Existen {Pato.cantidad} patos")
print(f"En total hay {Pato.plumas} plumas")

print("Fin del programa ahora limpiaremos la memoria")
sleep(WAIT * 2)

print(f"El sobrino {sobrinos[0].nombre} tiene {sobrinos[0].patas} plumas")

perro = Perro()
perro.ladra()
print()
sleep(WAIT * 2)

animales = [
    Pato("Donald"),
    Pato("Daisy"),
    Perro(),
    Pato(),
    Perro()
]

for animal in animales:
    print(f"El animal tiene {animal.patas} patas")
    sleep(WAIT)

print()
print()
