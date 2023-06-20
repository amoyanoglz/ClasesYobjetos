from random import randint
from centro_educativo import CentroEducativo

if __name__ == "__main__":
    scale = randint(1, 100)
    alumnos = randint(8, 60) * scale
    profesores = randint(1, 10) * scale
    aulas = randint(1, 10) * scale

    centro_1 = CentroEducativo(alumnos, profesores, aulas)
    centro_1.puntuar()
    centro_1.listar()
    centro_1.convocar()
